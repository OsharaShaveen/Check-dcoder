import os
import telebot
from pyrogram


bot = telebot.TeleBot("5092293428:AAEViJbsdhTHIqcLU_WZNr_v-U3cB8DqKdQ")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Ehi Download Bot Made By Using Python3")


@bot.message_handler(commands=["info"])
def send_message(message):
  bot.send_message(message.chat.id, "Im Ehi Bot, You Can Download Ehi Files Using Me.. 😇 My Master Is WhiteDevil, He Makes Me Using Python3, Made In Sri lanka 🇱🇰")
  
@bot.on_message(filters.command('photo'))
def command1(bot, message):
    bot.send_photo(message.chat.id, "https://telegra.ph/file/b843420e01298c0fb9712.jpg")

print("I AM ALIVE")
bot.run()
