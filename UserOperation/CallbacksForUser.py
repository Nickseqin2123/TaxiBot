from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from SqlReq.RedReq import redis_get
from SqlReq.SecondRequests import database
from driver import DRIVER_ID
from Keyboards.keyboards import for_driver, cancel_order, menu
from UserOperation.taxi_ordering import messages_cls


router = Router(name=__name__)
bot = Bot(token='7051292123:AAF5SrWp00cLQXyh4MhhXDrv-iZGk1r-jXE')


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
        callback.message.chat.id,
        messages_cls.for_user_id
    )
    
    await bot.delete_message(
        DRIVER_ID,
        messages_cls.for_driver_id
    )
        
    await callback.message.delete()
    
    database.del_orders(
        callback.from_user.id
    )

    await callback.message.answer(
        text="Сообщение удалено у водителя",
        reply_markup=await menu()
    )