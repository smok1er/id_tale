import telebot
import flask
from flask import FLASK
from telebot import types 

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

Z1 = '\033[2;31m' #احمر ثاني

F = '\033[2;32m' #اخضر

A = '\033[2;34m'#ازرق

C = '\033[2;35m' #وردي

B = '\033[2;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح

server = Flask(__name__)
token = "5590751236:AAGjlo8vQE2TKLEUGcuxLWcgYI1B6z1k7Is"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):

  bot.send_message(message.chat.id,"*مرحبا ويهلا تريد تعرف شخص عن طريق الايدي ؟وصلت* /id\n\n*BY :* @C_P_8",parse_mode='markdown')

@bot.message_handler(commands=['id'])

def id(message):

  bot.send_message(message.chat.id,f"*ID :* `{message.chat.id}`",parse_mode='markdown')

@bot.message_handler(commands=['info'])

def info(message):

  bot.send_message(message.chat.id,f"*مرحبا ويهلا تريد تعرف شخص عن طريق الايدي ؟وصلت* /id\n\n*BY :* @C_P_8",parse_mode='markdown')

@bot.message_handler(content_types=['text'])

def start1(message):

  bot.send_message(message.chat.id,"*يلا خيي دز ايدي* /id\n\n*BY : @C_P_8*",parse_mode='markdown')
@server.route(f"/{token}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://nziid.herokuapp.com/"+str(token))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.infinity_polling()
