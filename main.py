import os
import telebot


bot = telebot.TeleBot("5074526105:AAGi244pOawYoCf4IfJDkMxHWa3BduZDpPA")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Chat Bot Made By Using Python3")


@bot.message_handler(commands=["info"])
def send_message(message):
  bot.send_message(message.chat.id, "Im Ehi Bot, You Can Chat  Me.. 😇 My Master Is WhiteDevil, He Makes Me Using Python3, Made In Sri lanka 🇱🇰")



bot.polling()
