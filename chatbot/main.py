import telegram

api_key ='762857482:AAH1wUdMnx_wITx_IC1wKJWV2ozAW_keLNY'

bot = telegram.Bot (token = api_key)

# chat_id = bot.get_updates() [-1].message.chat_id
chat_id = 819836364

print(chat_id)

bot.sendMessage(chat_id = chat_id, text="안녕")
