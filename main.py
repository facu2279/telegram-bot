""" Hecho por Facundo Diaz 19/05/2021 """


""" IMPORTS """
"""pyTelegramBotAPI module"""
import telebot
""" requests module"""
import requests


""" el user name del bot es @weather_nerv_bot
la version que queda subida en github no va a tener seteada
la variable API_KEY para evitar que alguien modifique su funcionalidad """

API_KEY = "1780454391:AAEvdNwlIt_3n3HHyLs21GEzV8rwduRdJRs"
i = 0

""" creamos la instancia """
bot = telebot.TeleBot(API_KEY)


""" convertir grados kelvin to celcius """
def kelvin_to_c(temp):
  temp =  int(temp - 273.15)
  return temp


""" hace un request a https://openweathermap.org/api y nos retorna un description
con info y otros dict, saco los datos que necesito y los concateno para retornar
el string que quiero imprimir en el chat luego"""
def info_clima(pais):
  query = "http://api.openweathermap.org/data/2.5/weather?q="
  query2 = "&appid=b01d355c0ce08cde0aed9ad580d0c649"
  r = requests.get(query + pais + query2)
  r = r.json()
  inicio = "The weather in " + pais + " is "
  descripcion = r["weather"]
  for i in descripcion:
      for i2 in i:
          if i2 == "description":
              descripcion = i[i2]
  temperatura = (r["main"]["temp"])
  temperatura = kelvin_to_c(temperatura)
  presion = (r["main"]["pressure"])
  humedad = (r["main"]["humidity"])
  strfinal = str(inicio) +  str(descripcion) + " with a temperature of " +  str(temperatura) + "*C and atmospheric pressure is " + str(presion) + '" and the humidity in the air is ' + str(humedad) + "%"
  return strfinal



""" start function - muestra en pantalla el menu prinicipal """
@bot.message_handler(commands=['start'])
def menu(message):
  bot.send_message(message.chat.id, "Hi! how can I help you?\n\nI want to know the /weather \nI want to /count or /restart the counter")



""" weather function - muestra las ciudades a las que podemos consultar el clima """
@bot.message_handler(commands=['weather'])
def climas(message):
  bot.send_message(message.chat.id, "Welcome to the weather section\n\nChoose a place\n\n/Montevideo\n/Londres\n/Madrid")


""" suma uno a la variable i que usamos para contar 
y luego lo printea en pantalla """
@bot.message_handler(commands=['count'])
def opcion2(message):
  global i
  i += 1
  string = "The number of times you counted is : " + str(i)
  bot.send_message(message.chat.id, string)

""" reset variable i to 0 """
@bot.message_handler(commands=['restart'])
def reset_counter(message):
  global i
  i = 0
  bot.send_message(message.chat.id, "The counter was reset to 0")


""" kit de funciones que llaman info_clima pasandole
como parametro distintos paises y luego muestra en pantalla la info"""
@bot.message_handler(commands=['Montevideo'])
def mvd(message):
  res = info_clima("Montevideo")
  bot.send_message(message.chat.id, res)

@bot.message_handler(commands=['Londres'])
def london(message):
  res = info_clima("London")
  bot.send_message(message.chat.id, res)

@bot.message_handler(commands=['Madrid'])
def madrid(message):
  res = info_clima("Madrid")
  bot.send_message(message.chat.id, res)

""" consulta constantemente """
bot.polling()
