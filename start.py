#!/usr/bin/python

# Import Module / Package External
import os, logging
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Chat

# Import Module / Package Internal
from tars import tools

# Load Semua Isi File .env
load_dotenv()

# Logging Config
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

bot = TeleBot(os.getenv('BOT_TOKEN'))

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.send_message(msg.from_user.id, """
Halo, Saya TARS Bot.
Saya bertugas sebagai alat bantu bagi Anda yang menginginkan bantuan saya. Berikut perintah untuk mendapatkan apa saja yang kami sediakan secara Umum!

/help = Lihat Seluruh Panduan Tools Yang Tersedia!
""")


# Handle All Message
@bot.message_handler(func=lambda msg: True)
def wrap_message(msg):
    cmd_list = ['/help', '/whois', '/nmap']

    if msg.text == cmd_list[0]:
        bot.send_message(msg.from_user.id, tools.__helpers())
    elif len(msg.text) >= 8:
        bot.send_message(msg.from_user.id, tools.__whois      (msg.text[8:]))
    elif len(msg.text) >= 7:
        getCmd = msg.text[7:].split('')
        bot.send_message(msg.from_user.id, tools.__nmap(host, port, arg))
    else:
        bot.send_message(msg.from_user.id, 'Perintah yang Anda masukkan tidak Valid! Silahkan coba lagi...')

# Banner
def bannerBot():
    return """
 _____  _    ____  ____  ____        _
|_   _|/ \  |  _ \/ ___|| __ )  ___ | |_                        | | / _ \ | |_) \___ \|  _ \ / _ \| __|
  | |/ ___ \|  _ < ___) | |_) | (_) | |_                        |_/_/   \_\_| \_\____/|____/ \___/ \__| | v1.0.0
    """

# Running Bot
if __name__ == '__main__':
    os.system('clear')
    print(bannerBot())
    logging.info('Bot Sudah Aktif :)')
    bot.infinity_polling()
