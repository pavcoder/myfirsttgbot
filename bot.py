import telebot
import random2
import os
from telebot import types
import pyowm
token = str(os.environ.get('968156969:AAHsqLoaRjcnaKZuLmboGIMr4LPlrV0KtM4'))
bot=telebot.TeleBot(token)
markup=types.ReplyKeyboardMarkup(row_width=3)
btn1=types.KeyboardButton('Привет')
btn2=types.KeyboardButton('Расскажи анекдот')
btn3=types.KeyboardButton(b"\xF0\x9F\x8E\xB2".decode("utf-8"))
btn4=types.KeyboardButton(b"\xF0\x9F\x98\x82".decode("utf-8"))
btn5=types.KeyboardButton('Скажи погоду')
btn6=types.KeyboardButton(b"\xF0\x9F\x92\xB0".decode("utf-8"))
markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
markup_2=types.ReplyKeyboardMarkup(row_width=1)
btn7=types.KeyboardButton('Спасибо')
markup_2.add(btn7)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я Гамма!",reply_markup=markup)
#@bot.middleware_handler(update_types=["message"])
#def modify_message(bot_instance,message):
#	message.another_text=message.text+':kek'
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	print(message.text)
	if message.text=="Привет":
		bot.send_message(message.chat.id, "Привет, друг!",reply_markup=markup)
	if (message.text=="Расскажи анекдот" or message.text=="/joke"):
		with open('jokes.txt','r') as nnn:
			joke = [line.strip() for line in nnn]
			nnn.close()
		ran=random2.choice(joke)
		bot.send_message(message.chat.id,ran,reply_markup=markup)
	if (message.text.startswith('/roll') or message.text.startswith(b"\xF0\x9F\x8E\xB2".decode("utf-8"))):
		message.text.strip(" ")
		print(message.text)
		bot.send_message(message.chat.id,random2.randint(1,100),reply_markup=markup)
	if message.text==b"\xF0\x9F\x92\xB0".decode("utf-8"):
		bot.send_message(message.chat.id,'money money money',reply_markup=markup)
	if message.text.lower()=="спасибо":
		bot.send_message(message.chat.id,'Всегда пожалуйста!',reply_markup=markup)
	if message.text==b"\xF0\x9F\x98\x82".decode("utf-8"):
		bot.send_message(message.chat.id,'Рад, что тебе весело!',reply_markup=markup)
	if message.text.lower()=='скажи погоду':
		owm =pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language="ru")
		place='Островец'
		weather_advice=""
		observation=owm.weather_at_place(place)
		w=observation.get_weather()
		veter=(str(round(w.get_wind()["speed"])))
		vlazhnost=(str(round(w.get_humidity())))
		temperatura=(str(round(w.get_temperature('celsius')["temp"])))
		if float(temperatura)<=15:
			weather_advice+="советую одеться потеплее "
		if float(veter)>=10:
			weather_advice+="сегодня ветренно "
		bot.send_message(message.chat.id,'В городе'+' '+place+' '+'сейчас'+' '+w.get_detailed_status()+', ветер'+' '+veter+' '+'метров в секунду'+', влажность'+' '+vlazhnost+' '+'процентов'+', температура'+' '+temperatura+' '+'градусов по Цельсию,'+weather_advice,reply_markup=markup_2)
		#bot.send_message(message.chat.id,reply_markup=markup_2)

bot.polling(none_stop=True)