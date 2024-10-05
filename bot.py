import telebot
from config import token
from random import choice

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['d6'])
def d6_handler(message):
    d6 = choice(["1", "2" ,"3" ,"4", "5", "6"])
    bot.reply_to(message, d6)

bot.infinity_polling()
