import telebot
import requests
import random
from bs4 import BeautifulSoup


bot = telebot.TeleBot('6014029819:AAGYTJuBJiSu6ZEOpIV6l60XorVW_U_UmfI')

@bot.message_handler(func=lambda message: True)
def send_random_image(message):
    # Obtiene la consulta de búsqueda del usuario
    search_query = message.text

    # Realiza una búsqueda en Google Imágenes
    search_url = f'https://www.google.com/search?q={search_query}&tbm=isch'
    response = requests.get(search_url)

    # Analiza el HTML de la respuesta de la búsqueda
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra todas las imágenes en la página
    images = soup.find_all('img')

    # Selecciona una imagen al azar
    random_image = random.choice(images)

    # Obtiene la URL de la imagen
    image_url = random_image['src']

    # Envía la imagen al usuario
    if image_url:
        bot.send_photo(message.chat.id, image_url)
    else:
        bot.reply_to(message, 'Lo siento, no se encontró ninguna imagen para tu búsqueda.')


# Iniciar el bot
bot.polling()