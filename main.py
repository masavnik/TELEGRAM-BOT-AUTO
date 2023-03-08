import telebot
from data import config
from button import calendar, auto, main_menu, info_shop, res_auto

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def main_button(message):
    main_menu(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'but1':
        auto(bot, call)
    if call.data == 'but2':
        calendar(bot, call)
    if call.data == 'but3':
        info_shop(bot, call)
    if call.data.startswith('auto'):
        res_auto(bot, call)


if __name__ == '__main__':
    bot.infinity_polling()
