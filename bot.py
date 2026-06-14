# =========================================
# IMPORT REQUIRED LIBRARIES
# =========================================

# os
# Used to safely read the BOT TOKEN
# from environment variables
import os

# telebot
# Main Telegram bot library
import telebot

# types
# Used for buttons and keyboard menus
from telebot import types


# =========================================
# BOT TOKEN
# =========================================

# Reads token from environment variable
# named BOT_TOKEN
TOKEN = os.getenv("BOT_TOKEN")

# Creates the bot object
bot = telebot.TeleBot(TOKEN)


# =========================================
# USER LANGUAGE STORAGE
# =========================================

# This dictionary stores each user's language
#
# Example:
# {
#   123456789: "english",
#   987654321: "amharic"
# }
#
# chat.id = key
# selected language = value
user_language = {}


# =========================================
# LANGUAGE MENU FUNCTION
# =========================================

# This function creates and returns
# the language selection buttons
def language_menu():

    # Creates inline keyboard
    # row_width=1 means one button per row
    markup = types.InlineKeyboardMarkup(row_width=1)

    # English button
    english_btn = types.InlineKeyboardButton(
        "🇬🇧 English",
        callback_data="english"
    )

    # Amharic button
    amharic_btn = types.InlineKeyboardButton(
        "🇪🇹 አማርኛ",
        callback_data="amharic"
    )

    # Oromo button
    oromo_btn = types.InlineKeyboardButton(
        "🟢 Afaan Oromo",
        callback_data="oromo"
    )

    # Add all buttons to keyboard
    markup.add(
        english_btn,
        amharic_btn,
        oromo_btn
    )

    # Return keyboard
    return markup


# =========================================
# MAIN MENU FUNCTION
# =========================================

# This function creates the main menu
# depending on selected language
def main_menu(lang):

    # Create keyboard
    markup = types.InlineKeyboardMarkup(row_width=1)

    # =====================================
    # ENGLISH MENU
    # =====================================
    if lang == "english":

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

    # =====================================
    # AMHARIC MENU
    # =====================================
    elif lang == "amharic":

        buyer_btn = types.InlineKeyboardButton(
            "🛒 ገዢ",
            callback_data="buyer"
        )

        seller_btn = types.InlineKeyboardButton(
            "🏪 ሻጭ",
            callback_data="seller"
        )

        about_btn = types.InlineKeyboardButton(
            "ℹ ስለ እኛ",
            callback_data="about"
        )

        back_btn = types.InlineKeyboardButton(
            "⬅ ተመለስ",
            callback_data="back_language"
        )

    # =====================================
    # OROMO MENU
    # =====================================
    elif lang == "oromo":

        buyer_btn = types.InlineKeyboardButton(
            "🛒 Bittaa",
            callback_data="buyer"
        )

        seller_btn = types.InlineKeyboardButton(
            "🏪 Gurguraa",
            callback_data="seller"
        )

        about_btn = types.InlineKeyboardButton(
            "ℹ Waa'ee",
            callback_data="about"
        )

        back_btn = types.InlineKeyboardButton(
            "⬅ Deebi'i",
            callback_data="back_language"
        )

    # Add buttons to keyboard
    markup.add(
        buyer_btn,
        seller_btn,
        about_btn,
        back_btn
    )

    # Return keyboard
    return markup


# =========================================
# START COMMAND
# =========================================

# Runs when user types /start
@bot.message_handler(commands=['start'])
def start(message):

    # Send logo image
    bot.send_photo(

        # Chat where message is sent
        message.chat.id,

        # Open logo image
        photo=open("logo.png", "rb"),

        # Caption text
        caption=
        "🌍 Choose Language\n\n"
        "ቋንቋ ይምረጡ\n\n"
        "Afaan filadhaa",

        # Attach language buttons
        reply_markup=language_menu()
    )


# =========================================
# CALLBACK QUERY HANDLER
# =========================================

# Handles ALL button clicks
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    # Get user chat id
    chat_id = call.message.chat.id

    # =====================================
    # ENGLISH SELECTED
    # =====================================
    if call.data == "english":

        # Save user language
        user_language[chat_id] = "english"

        # Edit existing message
        bot.edit_message_caption(

            # New caption
            caption=
            "🚀 Welcome to WagaBid!\n\n"
            "The Smart Reverse Auction Marketplace.",

            # Chat id
            chat_id=chat_id,

            # Message id to edit
            message_id=call.message.message_id,

            # Show English menu
            reply_markup=main_menu("english")
        )

    # =====================================
    # AMHARIC SELECTED
    # =====================================
    elif call.data == "amharic":

        # Save language
        user_language[chat_id] = "amharic"

        # Edit message
        bot.edit_message_caption(
            caption=
            "🚀 ወደ WagaBid እንኳን በደህና መጡ!\n\n"
            "ዘመናዊ የReverse Auction ገበያ",

            chat_id=chat_id,
            message_id=call.message.message_id,

            # Show Amharic menu
            reply_markup=main_menu("amharic")
        )

    # =====================================
    # OROMO SELECTED
    # =====================================
    elif call.data == "oromo":

        # Save language
        user_language[chat_id] = "oromo"

        # Edit message
        bot.edit_message_caption(
            caption=
            "🚀 Baga gara WagaBid dhuftan!\n\n"
            "Gabaa Reverse Auction ammayyaa.",

            chat_id=chat_id,
            message_id=call.message.message_id,

            # Show Oromo menu
            reply_markup=main_menu("oromo")
        )

    # =====================================
    # BACK TO LANGUAGE PAGE
    # =====================================
    elif call.data == "back_language":

        # Edit message back to language page
        bot.edit_message_caption(
            caption=
            "🌍 Choose Language\n\n"
            "ቋንቋ ይምረጡ\n\n"
            "Afaan filadhaa",

            chat_id=chat_id,
            message_id=call.message.message_id,

            # Show language buttons
            reply_markup=language_menu()
        )

    # =====================================
    # BUYER PAGE
    # =====================================
    elif call.data == "buyer":

        # Read saved language
        lang = user_language.get(chat_id)

        # ENGLISH
        if lang == "english":

            text = (
                "🛒 Buyer Section\n\n"
                "Post your request and receive offers from sellers."
            )

        # AMHARIC
        elif lang == "amharic":

            text = (
                "🛒 የገዢ ክፍል\n\n"
                "ጥያቄዎን ያቅርቡ እና ከሻጮች ዋጋ ይቀበሉ።"
            )

        # OROMO
        elif lang == "oromo":

            text = (
                "🛒 Kutaa Bittaa\n\n"
                "Gaaffii kee maxxansi fi gurgurtoota irraa dhiyeessa argadhu."
            )

        # Create back button
        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ Back",
            callback_data="main_menu"
        )

        markup.add(back_btn)

        # Edit message
        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================================
    # SELLER PAGE
    # =====================================
    elif call.data == "seller":

        # Get language
        lang = user_language.get(chat_id)

        # English text
        if lang == "english":

            text = (
                "🏪 Seller Section\n\n"
                "Compete with better prices and win buyers."
            )

        # Amharic text
        elif lang == "amharic":

            text = (
                "🏪 የሻጭ ክፍል\n\n"
                "በተሻለ ዋጋ ተወዳድረው ገዢዎችን ያሸንፉ።"
            )

        # Oromo text
        elif lang == "oromo":

            text = (
                "🏪 Kutaa Gurgurtaa\n\n"
                "Gatii fooyya'aa dhiyeessuun bitoota mo'adhaa."
            )

        # Create back button
        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ Back",
            callback_data="main_menu"
        )

        markup.add(back_btn)

        # Edit message
        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================================
    # ABOUT PAGE
    # =====================================
    elif call.data == "about":

        # Get language
        lang = user_language.get(chat_id)

        # English
        if lang == "english":

            text = (
                "ℹ WagaBid\n\n"
                "A reverse auction marketplace for Ethiopia."
            )

        # Amharic
        elif lang == "amharic":

            text = (
                "ℹ WagaBid\n\n"
                "ለኢትዮጵያ የReverse Auction ገበያ።"
            )

        # Oromo
        elif lang == "oromo":

            text = (
                "ℹ WagaBid\n\n"
                "Gabaa Reverse Auction Itoophiyaaf."
            )

        # Create keyboard
        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            "⬅ Back",
            callback_data="main_menu"
        )

        markup.add(back_btn)

        # Edit message
        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================================
    # RETURN TO MAIN MENU
    # =====================================
    elif call.data == "main_menu":

        # Get saved language
        lang = user_language.get(chat_id)

        # English
        if lang == "english":

            text = (
                "🚀 Welcome to WagaBid!\n\n"
                "The Smart Reverse Auction Marketplace."
            )

        # Amharic
        elif lang == "amharic":

            text = (
                "🚀 ወደ WagaBid እንኳን በደህና መጡ!"
            )

        # Oromo
        elif lang == "oromo":

            text = (
                "🚀 Baga gara WagaBid dhuftan!"
            )

        # Edit back to main menu
        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,

            # Show correct language menu
            reply_markup=main_menu(lang)
        )


# =========================================
# BOT START MESSAGE
# =========================================

print("🤖 WagaBid Bot is running...")


# =========================================
# KEEP BOT RUNNING FOREVER
# =========================================

bot.infinity_polling()
