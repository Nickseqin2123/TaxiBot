from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from RedisReq.RedReq import redis_get


router = Router(name=__name__)


@router.message(Command('tarifs'))
async def help_user(message: Message):
    tarif_day, tarif_night = redis_get('tarif_day'), redis_get('tarif_night')

    await message.answer(
        text=f"""Текущий тариф в днем: {int(tarif_day)} рублей на 1 км
Текущий тариф ночью: {int(tarif_night)} рублей на 1 км"""
    )