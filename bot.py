
import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


# START
@bot.message_handler(commands=['start'])
def start(message):

    # Show logo first
    bot.send_photo(
        message.chat.id,
        photo=open("logo.png", "rb")
    )

    # Language selector buttons
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    markup.row("🇬🇧 English")
    markup.row("🇪🇹 አማርኛ")
    markup.row("🇪🇹 Afaan Oromo")

    bot.send_message(
        message.chat.id,
        "Choose Language\n\n"
        "ቋንቋ ይምረጡ\n\n"
        "Afaan filadhaa",
        reply_markup=markup
    )


# LANGUAGE HANDLER
@bot.message_handler(func=lambda message: True)
def language_selector(message):

    if message.text == "🇬🇧 English":

        bot.send_message(
            message.chat.id,
            "Welcome to WagaBid 🚀"
        )

    elif message.text == "🇪🇹 አማርኛ":

        bot.send_message(
            message.chat.id,
            "ወደ WagaBid እንኳን በደህና መጡ 🚀"
        )

    elif message.text == "🇪🇹 Afaan Oromo":

        bot.send_message(
            message.chat.id,
            "Baga gara WagaBid dhuftan 🚀"
        )


print("🤖 Bot is running...")

bot.infinity_polling()
