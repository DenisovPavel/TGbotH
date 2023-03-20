import random
import time
import telebot
import json

token = 'по безопасности '

bot = telebot.TeleBot(token)
#global chislo
chislo = 0

with open("Гороскоп на сегодня.json",'w',encoding='utf-8') as horoscope:
    some_dict = json.load(horoscope)
    print(some_dict)

# @bot.message_handler(commands=['start']) # вызывается когда нажата команда старт
# def start(message):
#     bot.send_message(message.chat.id, "Приветствую! Путь к счастью кроется в твоих талантах! Как твои дела?") # приветствует
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Как дела?')
    item4 = telebot.types.KeyboardButton('Напоминание')
    item5 = telebot.types.KeyboardButton('Загадай число')
    item6 = telebot.types.KeyboardButton('Знак зодиака')
    item7 = telebot.types.KeyboardButton('Покажи id стикера')

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)



@bot.message_handler(content_types=['text']) # вызывается когда нажата команда старт
def answer(message):
  if message.text.lower() == 'отлично':
      bot.send_message(message.chat.id,"Так держать!Я очень рад за вас!")

  elif message.text.lower() == 'плохо':
      bot.send_message(message.chat.id,"Что произошло?.")

  elif message.text.lower() == 'знак зодиака':
      markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = telebot.types.KeyboardButton('Овен')
      item2 = telebot.types.KeyboardButton('Телец')
      item3 = telebot.types.KeyboardButton('Близнецы')
      item4 = telebot.types.KeyboardButton('Рак')
      item5 = telebot.types.KeyboardButton('Лев')
      item6 = telebot.types.KeyboardButton('Дева')
      item7 = telebot.types.KeyboardButton('Весы')
      item8 = telebot.types.KeyboardButton('Скорпион')
      item9 = telebot.types.KeyboardButton('Стрелец')
      item10 = telebot.types.KeyboardButton('Козерог')
      item11= telebot.types.KeyboardButton('Водолей')
      item12= telebot.types.KeyboardButton('Рыбы')
      markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
      bot.send_message(message.chat.id, 'Выбери свой знак!',reply_markup=markup)
      bot.register_next_step_handler(message,horo_check)


  elif message.text.lower() == 'как дела?':
      some_list=["хорошо","плохо","отлично","нормально","замечательно","волшебно","хуже некуда","топчик"]
      number=random.randint(0,len(some_list))
      bot.send_message(message.chat.id,some_list[number])

  elif message.text.lower() == 'загадай число':
      global chislo
      chislo = random.randint(1,10)
      bot.send_message(message.chat.id, "Число загадано!")
      bot.register_next_step_handler(message,chislo_checker())

  elif message.text.lower() == 'рандомное число':
      bot.send_message(message.chat.id,str(random.randint(1,10)))

  elif message.text.lower()=='напоминание':
      bot.send_message(message.chat.id, "Укажите время: ")
      bot.register_next_step_handler(message,timechecker)


  elif message.text.lower() == 'кинуть кость':
      bot.send_message(message.chat.id, str(random.randint(1, 7)))

  else:
      bot.send_message(message.chat.id,"Я еще не понимаю это, но скоро меня всему научат!")
  #  bot.send_message(message.chat.id, "Лучше пузо от пива, чем горб от работы!")

@bot.message_handler(content_types=['text']) # вызывается когда нажата команда старт
def timechecker(message):
    bot.send_message(message.chat.id,'Напоминание!Время подошло!')
    with open("time.txt",'w',encoding="utf-8")as file:
        file.write(str(message.chat.id))
        file.write(''+str(message.text))
# while True:
#     now =datetime.datetime.now()
#     current_time=now.strftime("%H:%M")
#     if current_time==times:
#         bot.send_message(int(chat),"Напоминание!Время подошло!")

@bot.message_handler(content_types=['text'])
def chislo_checker(message):
    if message.text.lower() != f'{chislo}':
        bot.send_message(message.chat.id, "Не верно!Пробуй еще!")
        bot.register_next_step_handler(message, chislo_checker) # если не угадывает он слушает еще раз
    else:
        bot.send_message(message.chat.id, "Вы угадали число!Мои поздравления!")

@bot.message_handler(content_types=['text'])
def horo_check(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item13 = telebot.types.KeyboardButton('Стоп')
    markup.add(item13)
    if message.text == 'Стоп':
        bot.send_message(message.chat.id, some_dict[message.text], reply_markup=markup)
        bot.register_next_step_handler(message,horoscope)

bot.polling(none_stop=True) # при запуске модуля, бот будет бесконечно запущен