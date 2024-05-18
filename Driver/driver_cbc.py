from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from driver import DRIVER_ID, DRIVER_PHONE
from Keyboards.keyboards import cancel_order_in_driver, menu
from AsyncSQLReq.UserSql import database
from UserOperation.taxi_ordering import messages_cls


bot = Bot(token='7051292123:AAF5SrWp00cLQXyh4MhhXDrv-iZGk1r-jXE')
router = Router(name=__name__)


@router.callback_query(F.data == 'Apply')
async def accepy_order(callback: CallbackQuery):
    await bot.send_message(
        chat_id=DRIVER_ID,
        text="""Заказ приянт, выезжайте к пользователю.
Для связи можете использовать его ID или номер телефона""",
reply_markup=await cancel_order_in_driver()
    )
    await callback.message.answer(
        text=f'Водитель выехал к вам. Ожидайте. Номер телефона водителя: {DRIVER_PHONE}'
    )


@router.callback_query(F.data == 'Canceldriver')
async def not_go(callback: CallbackQuery):
    await callback.message.answer(
        text='Водитель отменил заказ',
        reply_markup=await menu()
    )
    await bot.delete_messages(
        callback.message.chat.id,
        [messages_cls.for_alt_user, 
        messages_cls.for_driver_id]
    )
    
    await database.del_orders(
        callback.from_user.id
    )