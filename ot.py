import telebot
from telebot import types

bot = telebot.TeleBot('1960569141:AAERTnz6OLPReFKdgTl2Y5WcSK1xq7klusE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, ты хочешь собрать себе ПК?")

    elif message.text.lower() == "да":
        bot.send_message(message.from_user.id, "тогда я тебе помогу")
        bot.send_message(message.from_user.id, "вы хотите собрать ПК в пределах 50к? 1 - да,2 - нет")
    if message.text == "1":
        bot.send_message(message.from_user.id, "для каких задач ПК? 3 - для игр,4 - для работ")
    elif message.text == "3":
        bot.send_message(message.from_user.id, "вы будете играть в новинки? 5 - да,6 - нет")
    elif message.text == "6":
        bot.send_message(message.from_user.id, "ссборка для вас")
        bot.send_message(message.from_user.id, "процессорINTEL Core i3 9100F  ссылка на ситилинк ---> https://clck.ru/Xe4Uz ")
        bot.send_message(message.from_user.id, "видеокарта asus PH-GTX1050TI-4G ссылка на ситилинк ---> https://clck.ru/Xe4iE ")
        bot.send_message(message.from_user.id, "RAM для вас  CRUCIAL CT8G4DFRA266 DDR4 - 8GB 2666 ссылка на ситилинк ---> https://clck.ru/Wxp8t ")
        bot.send_message(message.from_user.id, "материнская плата для вас GIGABYTE H310M S2, LGA 1151v2 ссылка на ситилинк ---> https://clck.ru/Xo49a ")
        bot.send_message(message.from_user.id,"блок питания для вас Aerocool VX PLUS 700W ссылка на сиитилинк ---> https://clck.ru/Xo55u ")
    if message.text == "1":
        bot.send_message(message.from_user.id, "для каких задач ПК? 3 - для игр,4 - для работ")
    elif message.text == "4":
        bot.send_message(message.from_user.id, "вы будете заниматься видео монтажем? 5 - да,6 - нет")
    elif message.text == "5":
        bot.send_message(message.from_user.id,"вы будете заниматься 3D моделированием? 7 - да,8 - нет")

bot.polling(none_stop=True, interval=0)

