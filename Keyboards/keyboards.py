from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


async def menu():
    buttons = ['Заказать такси']
    builder = ReplyKeyboardBuilder()

    for button_name in buttons:
        builder.button(
            text=button_name
        )

    return builder.as_markup(resize_keyboard=True)


async def contact_keyb():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text='📱 Отправить',
        request_contact=True
    )
    
    return builder.as_markup(resize_keyboard=True)


async def geo_keyb():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text='📍 Отправить',
        request_location=True,
    )
    builder.button(
        text='Главное меню'
    )

    return builder.as_markup(resize_keyboard=True)


async def only_go_menu():
    builder = ReplyKeyboardBuilder()

    builder.button(
        text='Главное меню'
    )

    return builder.as_markup(resize_keyboard=True)


async def get_inline_keyb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        InlineKeyboardButton(
            text="Отправить заказ водителю",
            callback_data=f'Driver'
        )
    )
    
    return builder.as_markup(resize_keyboard=True)


async def for_driver():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        InlineKeyboardButton(
            text="Принять заказ",
            callback_data='Apply'
        )
    )
    
    return builder.as_markup(resize_keyboard=True)


async def cancel_order():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        InlineKeyboardButton(
            text="Отменить заказ",
            callback_data=f'Cancel'
        )
    )
    
    return builder.as_markup(resize_keyboard=True)


async def cancel_order_in_driver():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        InlineKeyboardButton(
            text="Не поеду",
            callback_data=f'Canceldriver'
        )
    )
    
    return builder.as_markup(resize_keyboard=True)