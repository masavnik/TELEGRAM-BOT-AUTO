def add_button_info_shop(bot_token, call):
    with open('data/info_shop.txt', 'r', encoding='utf-8') as file:
        read = file.read()
    bot_token.send_message(call.from_user.id, read)