import telebot
from telebot import types
from data import config
import json


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def main_button(message):
    '''Функция, которая обрабатывает кнопку START'''
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Посмотреть автомобили', callback_data='btn1')
    button2 = types.InlineKeyboardButton(text='Записаться на TEST DRIVE', callback_data='btn2')
    button3 = types.InlineKeyboardButton(text='Посмотреть информацию об автосалоне', callback_data='btn3')
    buttons.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Здравствуйте, что вы хотите сделать?", reply_markup=buttons)


@bot.callback_query_handler(func=lambda c: True)
def ans(c):
    cid = c.message.chat.id
    if c.data == "btn1":
        with open('parser.json') as file:
            data_1 = json.load(file)

        new_list = []
        for i in data_1:
            new_list.append(i['AUTO'])

        keyboard = types.InlineKeyboardMarkup()
        buttons = types.InlineKeyboardMarkup(row_width=5)
        for y in new_list:
            button1 = types.InlineKeyboardButton(text=y, callback_data='btn43', row_width=5)
            buttons.add(button1, row_width=5)
        bot.send_message(c.from_user.id, 'Выберете автомобиль', reply_markup=buttons)


