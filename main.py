import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging
import re
import modulos

my_secret = os.environ['TELEGRAM_TOKEN']
TOKEN = my_secret

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s -%(message)s,")
logger = logging.getLogger()

mensaje_bienvenida = "! 👋 gracias por comunicarte con MENSAJERIA AA, tu domicilio de confianza 🏍💨. Si deseas un servicio por favor regalanos los siguientes datos: \n🔲📍Dirección de origen(Barrio, casa o edificio/apto)\nDirección de entrega(Barrio, casa o edificio/apto)\n🔲👤Nombre y de las personas que entregan y reciben(Especifica quien paga el servicio)\n🔲📦Tipo de producto que desea transportar\n✔El precio del servicio te lo facilitaremos de inmediato he iniciaremos luego de su confirmación"

mensaje_de_ejemplo = "Ejemplo:\n D1: Calle 76#44-31, Edificio La Seiba, apto 345\n D2: Calle 32#25-89, casa\nNombre1: Carlos Manuel Cervante\n Nombre2: El pato Elias "



def precio_pedido(update, context):
  mensaje = update.message.text
  d1 = re.search("D1:(.+[0-9]),", mensaje)
  d2 = re.search("D2:(.+[0-9]).,", mensaje)
  dir1 = str(d1.group(1))
  dir2 = str(d2.group(1))
  coordenadas_origen = modulos.geocode(dir1)
  coordenadas_destino = modulos.geocode(dir2)
  distancia = modulos.distancia(coordenadas_origen, coordenadas_destino)
  return distancia




def start(update, context):
    logger.info(
        f"El usuario {update.effective_user['username']}, ha iniciado una conversación"
    )
    name = update.effective_user['first_name']
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Hola {name}{mensaje_bienvenida}")

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=mensaje_de_ejemplo)
    dp.add_handler(MessageHandler(Filters.text, precio_pedido))


if __name__ == "__main__":
    #Obteniendo los datos
    my_bot = telegram.Bot(token=TOKEN)
    print(my_bot.getMe())

updater = Updater(my_bot.token, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
