# telegram에서 가능한 chatbot
# 나만의 여자친구 만들기
from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize

updater = Updater(token='762857482:AAH1wUdMnx_wITx_IC1wKJWV2ozAW_keLNY')
dispatcher = updater.dispatcher
updater.start_polling()

def handler(bot, update):
  text = update.message.text
  chat_id = update.message.chat_id
  
  if '뭐해' in text:
    bot.send_message(chat_id=chat_id, text='오빠 생각 ><')
  elif '몇시에만날래' in text:
    bot.send_message(chat_id=chat_id, text='7시에 보자')
  elif '아잉' in text:
    bot.send_message(chat_id=chat_id, text=emojize('아잉:heart_eyes:', use_aliases=True))
  elif '보고싶어' in text:
    bot.send_photo(chat_id=chat_id, photo=open('img/na.jpg', 'rb'))
  else:
    bot.send_message(chat_id=chat_id, text='몰라')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
