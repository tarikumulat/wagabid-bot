
import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


# START
@bot.message_handler(commands=['start'])
def start(message):

    # Show logo
    bot.send_photo(
        message.chat.id,
        photo=open("logo.png", "rb")
    )

    # Inline buttons
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "🇬🇧 English",
        callback_data="english"
    )

    btn2 = types.InlineKeyboardButton(
        "🇪🇹 አማርኛ",
        callback_data="amharic"
    )

    btn3 = types.InlineKeyboardButton(
        "🟢 Afaan Oromo",
        callback_data="oromo"
    )

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    bot.send_message(
        message.chat.id,
        "Choose Language",
        reply_markup=markup
    )


# BUTTON HANDLER
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "english":

        bot.send_message(
            call.message.chat.id,
            "Welcome to WagaBid 🚀"
        )

    elif call.data == "amharic":

        bot.send_message(
            call.message.chat.id,
            "ወደ WagaBid እንኳን በደህና መጡ 🚀"
        )

    elif call.data == "oromo":

        bot.send_message(
            call.message.chat.id,
            "Baga gara WagaBid dhuftan 🚀"
        )


print("🤖 Bot is running...")

bot.infinity_polling()
