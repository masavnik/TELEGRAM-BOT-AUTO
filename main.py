import telebot
from telebot import types
from data import config
import json

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def main_button(message):
    '''Функция, которая обрабатывает кнопку START'''
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='🚗Посмотреть автомобили🚗', callback_data='but1')
    button2 = types.InlineKeyboardButton(text='🖊Записаться на TEST DRIVE🖊', callback_data='but2')
    button3 = types.InlineKeyboardButton(text='😊Посмотреть информацию об автосалоне😊', callback_data='but3')
    buttons.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Здравствуйте, что вы хотите сделать?", reply_markup=buttons)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    with open('data\parser.json') as file:
        data_1 = json.load(file)
    if call.data == 'but1':
        list_auto = [i['AUTO'] for i in data_1]
        new_menu = types.InlineKeyboardMarkup(row_width=3)
        for i_auto in list_auto:
            new_menu.add(types.InlineKeyboardButton(i_auto, callback_data='but4'))
        bot.edit_message_text('Все автомобили в наличии', call.message.chat.id, call.message.message_id,
                              reply_markup=new_menu)


if __name__ == '__main__':
    bot.infinity_polling()
