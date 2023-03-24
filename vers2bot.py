import telebot
import json
import  requests
from bs4 import  BeautifulSoup as b
import random

token = 'according security'

bot = telebot.TeleBot(token)



with open("AVARII.json","r",encoding='utf-8') as avi:
    some_dict1=json.load(avi)
with open("POZHAR.json","r",encoding='utf-8') as poz:
    some_dict2=json.load(poz)
with open("GAZ.json","r",encoding='utf-8') as gaz:
    some_dict3=json.load(gaz)
with open("HUMANHELP.json","r",encoding='utf-8') as help1:
    some_dict4=json.load(help1)
with open("HelpMYSELF.json","r",encoding='utf-8') as help2:
    some_dict5=json.load(help2)
with open("PhoneNumbers.json", "r", encoding='utf-8') as pho:
     some_dict6 = json.load(pho)
with open("PSYHOHELP.json", "r", encoding='utf-8') as psy:
    some_dict7 = json.load(psy)
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Авария!')
    item2 = telebot.types.KeyboardButton('Пожар!')
    item3 = telebot.types.KeyboardButton('Утечка Газа!')
    item4 = telebot.types.KeyboardButton('Человеку плохо!')
    item5 = telebot.types.KeyboardButton('Мне стало плохо!')
    item6 = telebot.types.KeyboardButton('Тел-ны экст. служб!')
    item7 = telebot.types.KeyboardButton('Служба психологической поддержки!')
    item8 = telebot.types.KeyboardButton('Анекдот!')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
  if message.text == 'Авария!':
      markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) #создал кнопки(клаву)
      item1 = telebot.types.KeyboardButton('АВАРИИ НА Ж/Д')
      item2 = telebot.types.KeyboardButton('АВАРИИ НА АВТО')
      item3 = telebot.types.KeyboardButton('АВТО улетело в ВОДУ')
      item4 = telebot.types.KeyboardButton('АВАРИЯ САМОЛЕТА')
      item5 = telebot.types.KeyboardButton('АВАРИИ НА ВОДЕ')
      markup.add(item1, item2, item3, item4, item5)
      bot.send_message(message.chat.id, 'Выбери свой пункт!', reply_markup=markup) #добавил кнопки
      bot.register_next_step_handler(message,avariya)

  elif message.text == 'Пожар!':
      markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = telebot.types.KeyboardButton('Пожар в Доме')
      item2 = telebot.types.KeyboardButton('Пожар снаружи')
      item3 = telebot.types.KeyboardButton('Пожар в лифте')
      item4 = telebot.types.KeyboardButton('Пожар в транс-те')
      markup.add(item1, item2, item3, item4)
      bot.send_message(message.chat.id, 'Выбери свой пункт!', reply_markup=markup)
      bot.register_next_step_handler(message,pozhik)

  elif message.text == 'Утечка Газа!':
      markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = telebot.types.KeyboardButton("Почувствовал Газ")
      item2 = telebot.types.KeyboardButton('Утечка Газа')
      markup.add(item1, item2)
      bot.send_message(message.chat.id, 'Выбери свой пункт!', reply_markup=markup)
      bot.register_next_step_handler(message, gazik)

  elif message.text == 'Человеку плохо!':
      markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = telebot.types.KeyboardButton('Человек подавился')
      item2 = telebot.types.KeyboardButton('Судорожный приступ')
      item3 = telebot.types.KeyboardButton('Сердечный приступ')
      item4 = telebot.types.KeyboardButton('Потеря сознания')
      markup.add(item1, item2, item3, item4)
      bot.send_message(message.chat.id, 'Выбери свой пункт!', reply_markup=markup)
      bot.register_next_step_handler(message, helphu)

  elif message.text == 'Мне стало плохо!':
      markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = telebot.types.KeyboardButton('Поплохело на жаре')
      item2 = telebot.types.KeyboardButton('Поплохело в мороз')
      item3 = telebot.types.KeyboardButton('АВТО улетело в ВОДУ')
      markup.add(item1, item2, item3)
      bot.send_message(message.chat.id, 'Выбери свой пункт!', reply_markup=markup)
      bot.register_next_step_handler(message, helpme)

  elif message.text == 'Тел-ны экст. служб!':
      markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = telebot.types.KeyboardButton('Вызов ГБДД')
      item2 = telebot.types.KeyboardButton('Вызов Пожарных')
      item3 = telebot.types.KeyboardButton('Вызов Скорой')
      item4 = telebot.types.KeyboardButton('Вызов Газ.Сл.')
      item5 = telebot.types.KeyboardButton('Тел.Доверия')
      markup.add(item1, item2, item3, item4, item5)
      bot.send_message(message.chat.id, 'Выбери свой пункт!', reply_markup=markup)
      bot.register_next_step_handler(message,numbers)


  elif message.text== 'Служба психологической поддержки!':
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Агрессия")
    item2 = telebot.types.KeyboardButton("Депрессия")
    item3 = telebot.types.KeyboardButton("Страхи")
    item4 = telebot.types.KeyboardButton("Потеря интереса")
    item5 = telebot.types.KeyboardButton("Плохие мысли")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Выбери свой пункт!', reply_markup=markup)
    bot.register_next_step_handler(message, psy)

  elif message.text =='Анекдот!':
      bot.send_message(message.chat.id,"Здравствуйте! Чтобы прочитать анекдот введите любую цифру:")
      bot.message_handler(content_types=['text'])
      bot.register_next_step_handler(message, jokes)

  else:
      bot.send_message(message.chat.id, 'Выбери свой пункт!')

@bot.message_handler(content_types=['text']) #avarii
def avariya(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8 = telebot.types.KeyboardButton('Выход')
    markup.add(item8)
    if message.text != 'Выход':
        bot.send_message(message.chat.id, some_dict1[message.text], reply_markup=markup)
        bot.register_next_step_handler(message,avariya)

@bot.message_handler(content_types=['text']) #pozhar
def pozhik(message):
    bot.send_message(message.chat.id, some_dict2[message.text])
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8 = telebot.types.KeyboardButton('Выход')
    markup.add(item8)
    if message.text != 'Выход':
        bot.send_message(message.chat.id, some_dict2[message.text], reply_markup=markup)
        bot.register_next_step_handler(message,pozhik)

@bot.message_handler(content_types=['text']) #gazik
def gazik(message):
    bot.send_message(message.chat.id, some_dict3[message.text])
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8 = telebot.types.KeyboardButton('Выход')
    markup.add(item8)
    if message.text != 'Выход':
        bot.send_message(message.chat.id, some_dict3[message.text], reply_markup=markup)
        bot.register_next_step_handler(message,gazik)

@bot.message_handler(content_types=['text']) #humanhelp
def helphu(message):
    bot.send_message(message.chat.id, some_dict4[message.text])
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8 = telebot.types.KeyboardButton('Выход')
    markup.add(item8)
    if message.text != 'Выход':
        bot.send_message(message.chat.id, some_dict4[message.text], reply_markup=markup)
        bot.register_next_step_handler(message, helphu)

@bot.message_handler(content_types=['text']) #helpme
def helpme(message):
    bot.send_message(message.chat.id, some_dict5[message.text])
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8 = telebot.types.KeyboardButton('Выход')
    markup.add(item8)
    if message.text != 'Выход':
        bot.send_message(message.chat.id, some_dict5[message.text], reply_markup=markup)
        bot.register_next_step_handler(message, helpme)

@bot.message_handler(content_types=['text']) #phones
def numbers(message):
    bot.send_message(message.chat.id, some_dict6[message.text])
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8 = telebot.types.KeyboardButton('Выход')
    markup.add(item8)
    if message.text != 'Выход':
        bot.send_message(message.chat.id, some_dict6 [message.text], reply_markup=markup)
        bot.register_next_step_handler(message, numbers)

@bot.message_handler(content_types=['text']) #psyho
def psy(message):
    bot.send_message(message.chat.id, some_dict7[message.text])
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8 = telebot.types.KeyboardButton('Выход')
    markup.add(item8)
    if message.text != 'Выход':
        bot.send_message(message.chat.id, some_dict7 [message.text], reply_markup=markup)
        bot.register_next_step_handler(message, psy)

@bot.message_handler(content_types=['text']) #anekdots
def jokes(message):
    if message.text.lower() in "123456789":
        bot.send_message(message.chat.id,list_jokes[0])
        del list_jokes[0]
    else:
        bot.send_message(message.chat.id, " Введите цифру от 1-9! ")
URL = "https://www.anekdot.ru/last/good/"
def parser(url):
    r = requests.get(url)
    soup = b(r.text, "html.parser")
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]
list_jokes = parser(URL)
random.shuffle(list_jokes)


bot.polling(none_stop=True)