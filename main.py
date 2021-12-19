import os
import telebot


bot = telebot.TeleBot("5034975242:AAEXLY_YNKTo3D8t0j8PZDeVw6Pn_t6wSmE")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Chat Bot Made By Using Python3")


@bot.message_handler(commands=["info"])
def send_message(message):
  bot.send_message(message.chat.id, "Im Ehi Bot, You Can Chat  Me.. 😇 My Master Is WhiteDevil, He Makes Me Using Python3, Made In Sri lanka 🇱🇰")



bot.polling()
