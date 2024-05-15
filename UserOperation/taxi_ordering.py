from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from Keyboards.keyboards import (menu,
                                 geo_keyb,
                                 only_go_menu,
                                 get_inline_keyb,
                                 for_driver,
                                 cancel_order)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from SqlReq.SecondRequests import database
from UserOperation.get_km import ge
from driver import DRIVER_ID
from SqlReq.RedReq import redis_get
from dataclasses import dataclass, field


router = Router(name=__name__)
bot = Bot(token='7051292123:AAF5SrWp00cLQXyh4MhhXDrv-iZGk1r-jXE')


class GetInfo(StatesGroup):
    locationA = State()
    locationB = State()
    go_menu = State()
    

@dataclass
class MessagesId:
    for_driver_id: int = field(init=False)
    for_user_id: int = field(init=False)


messages_cls = MessagesId()


@router.message(F.text == 'Заказать такси', F.func(lambda x:
    bool(database.get_user_phone(x.from_user.id))
    and bool(database.get_orders(x.from_user.id)) is False))
async def taxi_get(message: Message, state: FSMContext):
    await state.set_state(GetInfo.locationA)
    
    await message.answer(
        text="""Итак, приступим к заказу, для начала укажи свое местоположение отправив 
свою геолокацию по кнопке '📍 Отправить'""",
reply_markup=await geo_keyb()
    )
    

@router.message(F.text == "Главное меню")
async def go_home(message: Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state is None:
        return
    
    await state.clear()
    await message.answer(
        text="Мы в меню",
        reply_markup=await menu()
    )


@router.message(GetInfo.locationA, F.location)
async def get_loca(message: Message, state: FSMContext):
    await state.update_data(locationa=message.location)
    
    await state.set_state(GetInfo.locationB)
    
    await message.answer(
        text="Отлично, теперь отправь мне геолокацию пункта назначения", 
        reply_markup=await only_go_menu()
    )


@router.message(GetInfo.locationB, F.location)
async def get_locb(message: Message, state: FSMContext):
    await state.update_data(locationb=message.location)
    
    
    data = await state.get_data()
    
    await state.clear()
    await summary(message, data, state)


async def summary(message: Message, data: dict, state: FSMContext):
    pointA = data['locationa']
    pointB = data['locationb']
    
    await message.answer(
        text="Идет расчет стоймости"
    )
    await state.set_state(GetInfo.go_menu)
    
    resp = await ge(pointA, pointB)
    
    for_user = await message.answer(
        text=f"{resp}", reply_markup=await get_inline_keyb()
    )
    
    messages_cls.for_user_id = for_user.message_id


@router.callback_query(F.data == "Driver")
async def send_driver(callback: CallbackQuery):
    
    mess = callback.message.text.split('|')
    
    user = callback.from_user.username
    
    user_num = redis_get(callback.from_user.id)
    
    driver_message = f"""Заказ № 000000
Пользователь: @{user}
----------------------------------------------

Номер телефона @{user}: +{int(user_num)}

Пункт назначения: {mess[3]}\n
Расстояние: {mess[5]}
{mess[-1]} по текущему тарифу

@{user} ждет вас по адресу: {mess[1]}"""

    database.regist_order(
        callback.from_user.id,
        driver_message
    )
    
    
    send_user = await bot.send_message(
        chat_id=DRIVER_ID,
        text=driver_message,
        reply_markup=await for_driver()
        )

    messages_cls.for_driver_id = send_user.message_id
    
    await callback.message.answer(
        text="Заказ был отправлен водителю",
        reply_markup=await cancel_order()
    )
    

@router.callback_query(F.data.split()[0] == 'Cancel')
async def del_message(callback: CallbackQuery):

    await bot.delete_message(
        DRIVER_ID,
        messages_cls.for_driver_id
    )
    
    await bot.delete_message(
        callback.message.chat.id,
        messages_cls.for_user_id
    )
        
    await callback.message.delete()
    
    database.del_orders(
        callback.from_user.id
    )

    await callback.message.answer(
        text="Сообщение удалено у водителя"
    )
    