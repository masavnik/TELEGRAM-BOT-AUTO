from telebot import types
from data import config
import json


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


def add_button_auto(bot_token, call):
    with open('data\parser.json') as file:
        data_1 = json.load(file)
    row = []
    list_auto_name = [i['AUTO'] for i in data_1]
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_back = types.InlineKeyboardButton(text='Назад',
                                             callback_data='back')

    for i, y in enumerate(list_auto_name):
        row.append(types.InlineKeyboardButton(text=f'{i + 1} - {y}',
                                              callback_data=f'{i + 1}'))
    markup.add(*row, button_back)
    bot_token.edit_message_text('Все автомобили в наличии\n'
                                'Выберете автомобиль',
                                call.message.chat.id,
                                call.message.message_id,
                                reply_markup=markup)
    return markup


def add_button_calendar(bot_token, call):
    button_calendar = types.InlineKeyboardMarkup(row_width=1)
    button_calendar.add(types.InlineKeyboardButton(text='На какой день вас записать?',
                                                   callback_data='j'))
    bot_token.edit_message_text('Выберете дату',
                                call.message.chat.id,
                                call.message.message_id,
                                reply_markup=button_calendar)
    return button_calendar


def add_button_info_shop(bot_token, call):
    with open('data\info_shop.txt', 'r', encoding='utf-8') as file:
        read = file.read()
    bot_token.send_message(call.from_user.id, read)