import telebot
from data import config
from button import \
    add_button_main_menu, \
    add_button_auto,\
    add_button_calendar,\
    add_button_info_shop

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def main_button(message):
    add_button_main_menu(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'but1':
        add_button_auto(bot, call)
    if call.data == 'but2':
        add_button_calendar(bot, call)
    if call.data == 'but3':
        add_button_info_shop(bot, call)


@bot.message_handler(commands=['but1'])
def low_price_city_request(message):
    bot.send_message(message.chat.id, 'Make your choice:')


if __name__ == '__main__':
    bot.infinity_polling()
