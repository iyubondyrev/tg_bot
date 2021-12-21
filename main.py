import telebot
import os
import random

MY_TOKEN = os.getenv("BOT_API_TOKEN")
bot = telebot.TeleBot(MY_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, i'm very stupid bot!\n"
                          "I can only send dudes\n"
                          "Write me anything and i'll show you")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    files = os.walk("dudes_storage/").__next__()[2]
    file_name = random.choice(files)
    dude = open("dudes_storage/" + file_name, 'rb')
    bot.send_photo(message.chat.id, dude, caption="Dude for you ;)")


bot.infinity_polling()
