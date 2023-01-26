import telebot
import config
from telebot import types
import os
bot = telebot.TeleBot('5837959249:AAFhR1t8RQ7bHm9Tqkp_pROqMI4obuQxLso')
@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("💧 Цены")
  btn2 = types.KeyboardButton("📊 Акции")
  markup.add(btn1, btn2)
  bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для парсинга сайтов по воде".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
  if(message.text == "💧 Цены"):
    bot.send_message(message.chat.id, text="Выполняется парсинг, немного подождите")
    os.system("python TESTFINAL.py")   
    with open("C:\\Users\\dmitr\\parsing.xlsx", "rb") as f1:
      bot.send_document(message.chat.id, f1)
  elif(message.text == "📊 Акции"):
    bot.send_message(message.chat.id, text="Выполняется парсинг акций, немного подождите")
    os.system("python 1.py")   
    with open("C:\\Users\\dmitr\\proj.xlsx", "rb") as f1:
      bot.send_document(message.chat.id, f1)
    with open("C:\\Users\\dmitr\\Аквамобиль.png", "rb") as f1:
      bot.send_photo(message.chat.id, f1)
    with open("C:\\Users\\dmitr\\Чебаркуль.png", "rb") as f1:
      bot.send_photo(message.chat.id, f1)
    with open("C:\\Users\\dmitr\\Чебаркуль2.png", "rb") as f1:
      bot.send_photo(message.chat.id, f1)

bot.polling(none_stop=True)

