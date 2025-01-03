from aiogram import Router, F
from aiogram.types import Message
from Keyboards.keyboards import (menu,
                                 geo_keyb,
                                 only_go_menu,
                                 get_inline_keyb,)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from AsyncSQLReq.UserSql import database
from UserOperation.get_km import ge
from dataclasses import dataclass, field


router = Router(name=__name__)


class GetInfo(StatesGroup):
    locationA = State()
    locationB = State()
    go_menu = State()
    

@dataclass
class MessagesId:
    for_driver_id: int = field(init=False)
    for_user_id: int = field(init=False)
    for_alt_user: int = field(init=False)


messages_cls = MessagesId()


@router.message(F.text == 'Заказать такси')
async def taxi_get(message: Message, state: FSMContext):
    if bool(await database.get_user_phone(message.from_user.id)) and \
    bool(await database.get_orders(message.from_user.id)) is False:
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