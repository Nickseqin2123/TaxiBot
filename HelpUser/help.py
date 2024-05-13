from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message


router = Router(name=__name__)


@router.message(Command('help'))
async def help_for_user(message: Message):
    await message.answer(
        text="""Как правильно заказать такси:
1.Перейдите во вкладку 'Заказать такси'.
2.Следуйте дальнейшей инструкцией по заказу.
3.Ожидайте принятия заказа.
Служба поддержки -> @Yorichi993"""
    )