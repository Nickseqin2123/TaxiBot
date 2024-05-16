from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from driver import DRIVER_ID
from Keyboards.keyboards import cancel_order_in_driver, menu
from SqlReq.SecondRequests import database


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
        text='Водитель выехал к вам. Ожидайте'
    )


@router.callback_query(F.data == 'Canceldriver')
async def not_go(callback: CallbackQuery):
    await callback.message.answer(
        text='Водитель отменил заказ',
        reply_markup=await menu()
    )
    
    database.del_orders(
        callback.from_user.id
    )