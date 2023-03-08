from telebot import types
from data import open_file_json


def add_button_auto(bot_token, call):
    data_auto = open_file.open_file_json_auto()
    row = []
    list_auto_name = [i['AUTO'] for i in data_auto]
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_back = types.InlineKeyboardButton(text='Назад',
                                             callback_data='back')

    for i, y in enumerate(list_auto_name):
        row.append(types.InlineKeyboardButton(text=f'{i + 1} - {y}',
                                              callback_data=f'auto' + y))

    markup.add(*row, button_back)
    bot_token.edit_message_text('Все автомобили в наличии\n'
                                'Выберете автомобиль',
                                call.message.chat.id,
                                call.message.message_id,
                                reply_markup=markup)

    return markup