import telebot
import os

#MY_TOKEN = os.getenv("BOT_API_TOKEN")
bot = telebot.TeleBot("5031732417:AAHERiilS6y7Lx95QpSs5_UnmdZg4_JbLDs")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
