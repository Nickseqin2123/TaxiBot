from aiogram.utils.keyboard import ReplyKeyboardBuilder


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