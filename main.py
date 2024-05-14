import asyncio
import logging

from aiogram import Dispatcher, Bot, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from Keyboards.keyboards import contact_keyb, menu
from main_router import router as main_router
from SqlReq.SqlRequests import database


dp = Dispatcher()
dp.include_router(
    main_router
)
bot = Bot(token='7051292123:AAF5SrWp00cLQXyh4MhhXDrv-iZGk1r-jXE')


class GetPhone(StatesGroup):
    phone_number = State()


@dp.message(CommandStart())
async def start_menu(message: Message, state: FSMContext):
    if bool(database.get_user_phone(
        message.from_user.id
    )):
        await message.answer(
            text='''Рад приветствовать тебя снова.С тарифами можно ознакомится по команде /tarifs.
Для помощи с заказом можно воспользоваться командой /help''',
reply_markup=await menu()
        )
    else:
        await state.set_state(GetPhone.phone_number)
        
        await message.answer(
            text='''Привет, это бот для заказа такси.
Для начала мне нужен твой номер телефона, чтобы
Водитель мог с тобой связаться. Нажми на кнопку "📱 Отправить", чтобы поделиться
своим номером телефона''', reply_markup=await contact_keyb() 
        )


@dp.message(GetPhone.phone_number, F.contact)
async def get_num(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    
    data = await state.get_data()
    await state.clear()
    
    await summary(message, data)


async def summary(message: Message, data: dict):
    database.set_user_phone(
        message.from_user.id,
        data['number']
    )
    
    await message.answer(
        text="""Номер телефона был успешно зарегестрирован.
С тарифами можно ознакомится по команде /tarifs.
Для помощи с заказом можно воспользоваться командой /help""",
reply_markup=await menu()
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())