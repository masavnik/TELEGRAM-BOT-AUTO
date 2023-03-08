from telebot import types


def add_button_calendar(bot_token, call):

    button_calendar = types.InlineKeyboardMarkup(row_width=1)
    button_calendar.add(types.InlineKeyboardButton(text='На какой день вас записать?',
                                                   callback_data='j'))
    bot_token.edit_message_text('Выберете дату',
                                call.message.chat.id,
                                call.message.message_id,
                                reply_markup=button_calendar)