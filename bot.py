import os
import telebot
from telebot import types

# =========================
# BOT TOKEN
# =========================
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    # Show Logo
    bot.send_photo(
        message.chat.id,
        photo=open("logo.png", "rb")
    )

    # Inline Language Buttons
    markup = types.InlineKeyboardMarkup(row_width=1)

    english_btn = types.InlineKeyboardButton(
        "🇬🇧 English",
        callback_data="english"
    )

    amharic_btn = types.InlineKeyboardButton(
        "🇪🇹 አማርኛ",
        callback_data="amharic"
    )

    oromo_btn = types.InlineKeyboardButton(
        "🇪🇹 Afaan Oromo",
        callback_data="oromo"
    )

    markup.add(
        english_btn,
        amharic_btn,
        oromo_btn
    )

    bot.send_message(
        message.chat.id,
        "Choose Language\n\n"
        "ቋንቋ ይምረጡ\n\n"
        "Afaan filadhaa",
        reply_markup=markup
    )


# =========================
# LANGUAGE HANDLER
# =========================
@bot.callback_query_handler(func=lambda call: True)
def language_selector(call):

    # Remove old buttons
    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=None
    )

    # ENGLISH
    if call.data == "english":

        bot.send_message(
            call.message.chat.id,
            "🚀 Welcome to WagaBid!\n\n"
            "The Smart Reverse Auction Marketplace."
        )

    # AMHARIC
    elif call.data == "amharic":

        bot.send_message(
            call.message.chat.id,
            "🚀 ወደ WagaBid እንኳን በደህና መጡ!\n\n"
            "ዘመናዊ የReverse Auction ገበያ"
        )

    # OROMO
    elif call.data == "oromo":

        bot.send_message(
            call.message.chat.id,
            "🚀 Baga gara WagaBid dhuftan!\n\n"
            "Gabaa Reverse Auction ammayyaa."
        )


# =========================
# RUN BOT
# =========================
print("🤖 WagaBid Bot is running...")

bot.infinity_polling()
