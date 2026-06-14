import os
import telebot
from telebot import types

# =========================
# BOT TOKEN
# =========================
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


# =========================
# LANGUAGE MENU FUNCTION
# =========================
def language_menu():

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
        "🟢 Afaan Oromo",
        callback_data="oromo"
    )

    markup.add(
        english_btn,
        amharic_btn,
        oromo_btn
    )

    return markup


# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    bot.send_photo(
        message.chat.id,
        photo=open("logo.png", "rb"),
        caption=
        "🌍 Choose Language\n\n"
        "ቋንቋ ይምረጡ\n\n"
        "Afaan filadhaa",
        reply_markup=language_menu()
    )


# =========================
# CALLBACK HANDLER
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    # =====================
    # ENGLISH MENU
    # =====================
    if call.data == "english":

        markup = types.InlineKeyboardMarkup(row_width=1)

        buyer_btn = types.InlineKeyboardButton(
            "🛒 Buyer",
            callback_data="buyer"
        )

        seller_btn = types.InlineKeyboardButton(
            "🏪 Seller",
            callback_data="seller"
        )

        about_btn = types.InlineKeyboardButton(
            "ℹ About",
            callback_data="about"
        )

        back_btn = types.InlineKeyboardButton(
            "⬅ Back",
            callback_data="back_language"
        )

        markup.add(
            buyer_btn,
            seller_btn,
            about_btn,
            back_btn
        )

        bot.edit_message_caption(
            caption=
            "🚀 Welcome to WagaBid!\n\n"
            "The Smart Reverse Auction Marketplace.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # AMHARIC MENU
    # =====================
    elif call.data == "amharic":

        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ ተመለስ",
            callback_data="back_language"
        )

        markup.add(back_btn)

        bot.edit_message_caption(
            caption=
            "🚀 ወደ WagaBid እንኳን በደህና መጡ!\n\n"
            "ዘመናዊ የReverse Auction ገበያ",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # OROMO MENU
    # =====================
    elif call.data == "oromo":

        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ Deebi'i",
            callback_data="back_language"
        )

        markup.add(back_btn)

        bot.edit_message_caption(
            caption=
            "🚀 Baga gara WagaBid dhuftan!\n\n"
            "Gabaa Reverse Auction ammayyaa.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # BACK TO LANGUAGE MENU
    # =====================
    elif call.data == "back_language":

        bot.edit_message_caption(
            caption=
            "🌍 Choose Language\n\n"
            "ቋንቋ ይምረጡ\n\n"
            "Afaan filadhaa",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=language_menu()
        )

    # =====================
    # BUYER PAGE
    # =====================
    elif call.data == "buyer":

        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ Back",
            callback_data="english"
        )

        markup.add(back_btn)

        bot.edit_message_caption(
            caption=
            "🛒 Buyer Section\n\n"
            "Post your request and receive offers from sellers.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # SELLER PAGE
    # =====================
    elif call.data == "seller":

        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ Back",
            callback_data="english"
        )

        markup.add(back_btn)

        bot.edit_message_caption(
            caption=
            "🏪 Seller Section\n\n"
            "Compete with better prices and win buyers.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # ABOUT PAGE
    # =====================
    elif call.data == "about":

        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ Back",
            callback_data="english"
        )

        markup.add(back_btn)

        bot.edit_message_caption(
            caption=
            "ℹ WagaBid\n\n"
            "A reverse auction marketplace for Ethiopia.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )


# =========================
# RUN BOT
# =========================
print("🤖 WagaBid Bot is running...")

bot.infinity_polling()
