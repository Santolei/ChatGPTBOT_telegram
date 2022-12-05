# Requisitos:
#   1. Tener una cuenta de Telegram y haber creado un bot de Telegram utilizando el BotFather.
#   2. Tener una cuenta de OpenAI y haber obtenido una clave de acceso a la API de ChatGPT.
#   3. Tener instalado Python 3 en el sistema.
#   4. Instalar los módulos de python `pyTelegramBotAPI` y `openai` utilizando pip.
#   5. Configurar el token del bot de Telegram y la clave de acceso a la API de ChatGPT en el script.
#   6. Ejecutar el script utilizando una conexión a Internet activa.

import telebot
import openai

# Inicializar la biblioteca openai utilizando tu secret key
openai.api_key = "TU SECRET KEY DE OPENAI"

# Obtener el token del bot de Telegram y crear un bot
bot = telebot.TeleBot(token="EL TOKEN QUE TE DA BOTFATHER DE TELEGRAM")

# Función para generar una respuesta utilizando la API de ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
)

    # Devolver la primera respuesta generada por ChatGPT
    return response["choices"][0]["text"]

# Establecer los comandos que el bot de Telegram puede aceptar
bot.set_my_commands([
    {
        "command": "/chatgpt",
        "description": "Enviar un mensaje al bot para que genere una respuesta utilizando la API de ChatGPT"
    }
])

# Procesar mensajes recibidos por el bot de Telegram
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Lista de IDs de usuarios autorizados, acá si ponés tu id de telegram vas a poder comunicarte vos y ninguna otra cuenta.
    # Para que eso funciono hay que descomentar el if y el else de más abajo.
    AUTHORIZED_USER_IDS = ['']
    # Verificar si el ID del usuario que envió el mensaje coincide con el ID del usuario autorizado
    # if message.from_user.id in AUTHORIZED_USER_IDS:
        # Obtener el texto del mensaje recibido
    text = message.text

    # Generar una respuesta utilizando la API de ChatGPT
    response = generate_response(text)

    # Enviar la respuesta generada al remitente del mensaje
    bot.send_message(chat_id=message.chat.id, text=response)
    #else:
        # Enviar un mensaje al usuario indicando que no está autorizado a recibir respuestas del bot
        #bot.send_message(chat_id=message.chat.id, text="You are not authorized to receive responses from this bot.")

# Iniciar el bot de Telegram
bot.polling()