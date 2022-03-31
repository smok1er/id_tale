import telebot

from telebot import types 

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

Z1 = '\033[2;31m' #احمر ثاني

F = '\033[2;32m' #اخضر

A = '\033[2;34m'#ازرق

C = '\033[2;35m' #وردي

B = '\033[2;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح

token = "5134782801:AAFSEsM-00Ink4Jsz0Q2g4tOZ9cOZ8Ea3Hg"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):

  bot.send_message(message.chat.id,"*Welcome to the bot to know your account ID Telegram to know your account ID send* /id\n\n*BY :* @HarithTools",parse_mode='markdown')

@bot.message_handler(commands=['id'])

def id(message):

  bot.send_message(message.chat.id,f"*ID :* `{message.chat.id}`",parse_mode='markdown')

@bot.message_handler(commands=['info'])

def info(message):

  bot.send_message(message.chat.id,f"*With this bot, you can get the ID of your Telegram account By sending* /id\n\n*BY :* @HarithTools",parse_mode='markdown')

@bot.message_handler(content_types=['text'])

def start1(message):

  bot.send_message(message.chat.id,"*To Get id send* /id\n\n*BY : @HarithTools*",parse_mode='markdown')

bot.infinity_polling()
