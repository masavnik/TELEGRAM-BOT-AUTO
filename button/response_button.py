from telebot import types
from data import open_file_json


def response_but(bot_token, call):
    of = open_file.open_file_json_auto()
    model_auto_button = bot_token.send_message(call.message.chat.id, call.data.replace('auto', ''))
    data_info_auto_list = []
    media_group = []
    for i in of:
        if model_auto_button.text == i['AUTO']:
            data_info_auto_list.append(i['AUTO'])
            data_info_auto_list.append(i['RUN'])
            data_info_auto_list.append(i['ENGINE'])
            data_info_auto_list.append(i['YEAR_OF_ISSUE'])
            data_info_auto_list.append(i['FUEL'])
            data_info_auto_list.append(str(i['PRICE']))
            for t in i['LINK']:
                media_group.append(types.InputMediaPhoto(t))

    bot_token.send_media_group(call.message.chat.id, media_group)
    bot_token.send_message(call.message.chat.id, text='\n'.join(data_info_auto_list))