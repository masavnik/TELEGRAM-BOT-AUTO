from telebot import types
from data import config


def add_button_main_menu(bot_token, message):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='🚗Посмотреть автомобили🚗', callback_data='but1')
    button2 = types.InlineKeyboardButton(text='🖊Записаться на TEST DRIVE🖊', callback_data='but2')
    button3 = types.InlineKeyboardButton(text='😊Посмотреть информацию об автосалоне😊', callback_data='but3')
    button4 = types.InlineKeyboardButton(text='Наш сайт', url=config.url)
    buttons.add(button1, button2, button3, button4)
    bot_token.send_message(message.chat.id,
                           f"Здравствуйте {message.chat.first_name}, что вы хотите сделать?",
                           reply_markup=buttons)
    return buttons