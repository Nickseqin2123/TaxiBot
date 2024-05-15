from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from SqlReq.SecondRequests import database


router = Router(name=__name__)


@router.message(Command('tarifs'))
async def help_user(message: Message):
    price = database.get_tar()[0]

    await message.answer(
        text=f"""Текущий тариф в днем: {price['tarif_day']} рублей на 1 км
Текущий тариф ночью: {price['tarif_night']} рублей на 1 км"""
    )