# =========================================================
# WAGABID BOT - VERSION UPGRADE NOTES
# =========================================================
#
# CHANGES MADE FROM PREVIOUS VERSION:
#
# 1. ADDED SQLITE DATABASE
# ---------------------------------------------------------
# Before:
# - User data was temporary
# - Everything disappeared when bot restarted
#
# Now:
# - User data is permanently stored
# - Bot remembers users after restart
# - Database file: wagabid.db
#
#
# 2. ADDED USERS TABLE
# ---------------------------------------------------------
# The bot now creates a real database table called:
#
# users
#
# Columns:
# - user_id
# - first_name
# - username
# - language
# - role
# - phone
# - joined_date
# - verified
#
#
# 3. ADDED NEW USER DETECTION
# ---------------------------------------------------------
# Before:
# - Bot treated everyone the same
#
# Now:
# - Bot checks if user already exists
#
# Example:
# IF user exists:
#     show "Welcome Back"
#
# ELSE:
#     create new account
#
#
# 4. ADDED RETURNING USER SYSTEM
# ---------------------------------------------------------
# Returning users now:
# - keep their language
# - skip language setup
# - go directly to main menu
#
#
# 5. ADDED LANGUAGE PERSISTENCE
# ---------------------------------------------------------
# Before:
# - Selected language disappeared after restart
#
# Now:
# - Language is saved in database permanently
#
#
# 6. IMPROVED NAVIGATION SYSTEM
# ---------------------------------------------------------
# Added:
# - Back buttons
# - Main menu navigation
# - Language switching
#
# Similar to:
# - BotFather
# - Professional Telegram bots
#
#
# 7. ADDED MULTI-LANGUAGE MENU SYSTEM
# ---------------------------------------------------------
# Entire bot now follows selected language:
#
# - Main menu
# - Buyer page
# - Seller page
# - About page
# - Back buttons
#
#
# 8. ADDED ACCOUNT FOUNDATION
# ---------------------------------------------------------
# This version now supports future features like:
#
# - Buyer accounts
# - Seller accounts
# - Phone verification
# - Orders
# - Offers/Bids
# - Payments
# - Ratings
# - Admin panel
#
#
# 9. DATABASE FOUNDATION
# ---------------------------------------------------------
# Bot architecture upgraded from:
#
# SIMPLE BOT
#
# to:
#
# REAL MULTI-USER MARKETPLACE SYSTEM
#
#
# 10. FUTURE EXPANSION READY
# ---------------------------------------------------------
# Next possible upgrades:
#
# - Role selection
# - Phone number collection
# - Buyer requests
# - Seller offers
# - Categories
# - Notifications
# - Escrow payments
# - Delivery system
#
# =========================================================


# =========================================================
# WAGABID TELEGRAM BOT
# MULTI LANGUAGE + SQLITE DATABASE + USER SYSTEM
# =========================================================


# =========================================================
# IMPORT LIBRARIES
# =========================================================

# Used for environment variables
import os

# SQLite database library
import sqlite3

# Used for dates
from datetime import datetime

# Telegram bot library
import telebot

# Used for buttons/keyboards
from telebot import types


# =========================================================
# BOT TOKEN
# =========================================================

# Reads bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN")

# Creates bot object
bot = telebot.TeleBot(TOKEN)


# =========================================================
# DATABASE CONNECTION
# =========================================================

# Creates/connects SQLite database
#
# wagabid.db will automatically be created
conn = sqlite3.connect(
    "wagabid.db",
    check_same_thread=False
)

# Cursor lets us execute SQL commands
cursor = conn.cursor()


# =========================================================
# CREATE USERS TABLE
# =========================================================

# Creates users table if it does not exist
cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    # Telegram unique user id
    user_id INTEGER PRIMARY KEY,

    # Telegram first name
    first_name TEXT,

    # Telegram username
    username TEXT,

    # Selected language
    language TEXT,

    # buyer / seller
    role TEXT,

    # User phone number
    phone TEXT,

    # Account creation date
    joined_date TEXT,

    # 0 = not verified
    # 1 = verified
    verified INTEGER DEFAULT 0

)

""")

# Saves database changes
conn.commit()


# =========================================================
# LANGUAGE MENU FUNCTION
# =========================================================

# Returns language selection buttons
def language_menu():

    # Creates inline keyboard
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

    # Add buttons
    markup.add(
        english_btn,
        amharic_btn,
        oromo_btn
    )

    # Return keyboard
    return markup


# =========================================================
# MAIN MENU FUNCTION
# =========================================================

# Returns main menu based on language
def main_menu(lang):

    # Create keyboard
    markup = types.InlineKeyboardMarkup(row_width=1)

    # =====================================================
    # ENGLISH
    # =====================================================
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
            "⬅ Change Language",
            callback_data="back_language"
        )

    # =====================================================
    # AMHARIC
    # =====================================================
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
            "⬅ ቋንቋ ቀይር",
            callback_data="back_language"
        )

    # =====================================================
    # OROMO
    # =====================================================
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
            "⬅ Afaan Jijjiiri",
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


# =========================================================
# START COMMAND
# =========================================================

# Runs when user types /start
@bot.message_handler(commands=['start'])
def start(message):

    # =====================================================
    # GET USER INFORMATION
    # =====================================================

    # Telegram unique user id
    user_id = message.from_user.id

    # Telegram first name
    first_name = message.from_user.first_name

    # Telegram username
    username = message.from_user.username

    # =====================================================
    # CHECK IF USER EXISTS
    # =====================================================

    cursor.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    # Gets user data
    user = cursor.fetchone()

    # =====================================================
    # NEW USER
    # =====================================================

    if user is None:

        # Current date
        joined_date = str(datetime.now().date())

        # Insert new user into database
        cursor.execute("""

        INSERT INTO users (

            user_id,
            first_name,
            username,
            joined_date

        )

        VALUES (?, ?, ?, ?)

        """, (

            user_id,
            first_name,
            username,
            joined_date

        ))

        # Save database
        conn.commit()

        # Send language selection page
        bot.send_photo(

            # Send to this chat
            message.chat.id,

            # Logo image
            photo=open("logo.png", "rb"),

            # Caption
            caption=
            "👋 Welcome New User!\n\n"
            "🌍 Choose Language\n\n"
            "ቋንቋ ይምረጡ\n\n"
            "Afaan filadhaa",

            # Language buttons
            reply_markup=language_menu()
        )

    # =====================================================
    # RETURNING USER
    # =====================================================

    else:

        # Get saved language
        saved_language = user[3]

        # If no language selected yet
        if saved_language is None:

            bot.send_photo(
                message.chat.id,
                photo=open("logo.png", "rb"),
                caption=
                "🌍 Choose Language",
                reply_markup=language_menu()
            )

        # If language already selected
        else:

            # English welcome
            if saved_language == "english":

                text = (
                    f"👋 Welcome Back {first_name}!\n\n"
                    "Welcome to WagaBid."
                )

            # Amharic welcome
            elif saved_language == "amharic":

                text = (
                    f"👋 እንኳን ደህና መጡ {first_name}!\n\n"
                    "ወደ WagaBid እንኳን በደህና መጡ።"
                )

            # Oromo welcome
            elif saved_language == "oromo":

                text = (
                    f"👋 Baga nagaan dhuftan {first_name}!\n\n"
                    "Gara WagaBid baga dhuftan."
                )

            # Send main menu directly
            bot.send_photo(
                message.chat.id,
                photo=open("logo.png", "rb"),
                caption=text,
                reply_markup=main_menu(saved_language)
            )


# =========================================================
# CALLBACK QUERY HANDLER
# =========================================================

# Handles ALL button clicks
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    # User chat id
    chat_id = call.message.chat.id

    # =====================================================
    # LANGUAGE SELECTION
    # =====================================================

    # English selected
    if call.data == "english":

        # Save language in database
        cursor.execute(
            """
            UPDATE users
            SET language=?
            WHERE user_id=?
            """,
            ("english", chat_id)
        )

        conn.commit()

        # Edit current message
        bot.edit_message_caption(
            caption=
            "🚀 Welcome to WagaBid!\n\n"
            "The Smart Reverse Auction Marketplace.",

            chat_id=chat_id,
            message_id=call.message.message_id,

            reply_markup=main_menu("english")
        )

    # =====================================================
    # AMHARIC
    # =====================================================

    elif call.data == "amharic":

        cursor.execute(
            """
            UPDATE users
            SET language=?
            WHERE user_id=?
            """,
            ("amharic", chat_id)
        )

        conn.commit()

        bot.edit_message_caption(
            caption=
            "🚀 ወደ WagaBid እንኳን በደህና መጡ!\n\n"
            "ዘመናዊ የReverse Auction ገበያ",

            chat_id=chat_id,
            message_id=call.message.message_id,

            reply_markup=main_menu("amharic")
        )

    # =====================================================
    # OROMO
    # =====================================================

    elif call.data == "oromo":

        cursor.execute(
            """
            UPDATE users
            SET language=?
            WHERE user_id=?
            """,
            ("oromo", chat_id)
        )

        conn.commit()

        bot.edit_message_caption(
            caption=
            "🚀 Baga gara WagaBid dhuftan!\n\n"
            "Gabaa Reverse Auction ammayyaa.",

            chat_id=chat_id,
            message_id=call.message.message_id,

            reply_markup=main_menu("oromo")
        )

    # =====================================================
    # BACK TO LANGUAGE PAGE
    # =====================================================

    elif call.data == "back_language":

        bot.edit_message_caption(
            caption=
            "🌍 Choose Language\n\n"
            "ቋንቋ ይምረጡ\n\n"
            "Afaan filadhaa",

            chat_id=chat_id,
            message_id=call.message.message_id,

            reply_markup=language_menu()
        )

    # =====================================================
    # BUYER PAGE
    # =====================================================

    elif call.data == "buyer":

        # Get saved language
        cursor.execute(
            "SELECT language FROM users WHERE user_id=?",
            (chat_id,)
        )

        lang = cursor.fetchone()[0]

        # English
        if lang == "english":

            text = (
                "🛒 Buyer Section\n\n"
                "Post requests and receive seller offers."
            )

            back_text = "⬅ Back"

        # Amharic
        elif lang == "amharic":

            text = (
                "🛒 የገዢ ክፍል\n\n"
                "ጥያቄ ያቅርቡ እና የሻጭ ዋጋ ይቀበሉ።"
            )

            back_text = "⬅ ተመለስ"

        # Oromo
        elif lang == "oromo":

            text = (
                "🛒 Kutaa Bittaa\n\n"
                "Gaaffii maxxansi fi dhiyeessa argadhu."
            )

            back_text = "⬅ Deebi'i"

        # Create keyboard
        markup = types.InlineKeyboardMarkup(row_width=1)

        # Back button
        back_btn = types.InlineKeyboardButton(
            back_text,
            callback_data="main_menu"
        )

        markup.add(back_btn)

        # Edit page
        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================================================
    # SELLER PAGE
    # =====================================================

    elif call.data == "seller":

        cursor.execute(
            "SELECT language FROM users WHERE user_id=?",
            (chat_id,)
        )

        lang = cursor.fetchone()[0]

        if lang == "english":

            text = (
                "🏪 Seller Section\n\n"
                "Compete with better prices."
            )

            back_text = "⬅ Back"

        elif lang == "amharic":

            text = (
                "🏪 የሻጭ ክፍል\n\n"
                "በተሻለ ዋጋ ተወዳደሩ።"
            )

            back_text = "⬅ ተመለስ"

        elif lang == "oromo":

            text = (
                "🏪 Kutaa Gurgurtaa\n\n"
                "Gatii fooyya'aa dhiyeessaa."
            )

            back_text = "⬅ Deebi'i"

        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            back_text,
            callback_data="main_menu"
        )

        markup.add(back_btn)

        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================================================
    # ABOUT PAGE
    # =====================================================

    elif call.data == "about":

        cursor.execute(
            "SELECT language FROM users WHERE user_id=?",
            (chat_id,)
        )

        lang = cursor.fetchone()[0]

        if lang == "english":

            text = (
                "ℹ WagaBid\n\n"
                "Smart Reverse Auction Marketplace."
            )

            back_text = "⬅ Back"

        elif lang == "amharic":

            text = (
                "ℹ WagaBid\n\n"
                "ዘመናዊ Reverse Auction ገበያ"
            )

            back_text = "⬅ ተመለስ"

        elif lang == "oromo":

            text = (
                "ℹ WagaBid\n\n"
                "Gabaa Reverse Auction ammayyaa."
            )

            back_text = "⬅ Deebi'i"

        markup = types.InlineKeyboardMarkup(row_width=1)

        back_btn = types.InlineKeyboardButton(
            back_text,
            callback_data="main_menu"
        )

        markup.add(back_btn)

        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # =====================================================
    # RETURN TO MAIN MENU
    # =====================================================

    elif call.data == "main_menu":

        cursor.execute(
            "SELECT language FROM users WHERE user_id=?",
            (chat_id,)
        )

        lang = cursor.fetchone()[0]

        if lang == "english":

            text = (
                "🚀 Welcome to WagaBid!"
            )

        elif lang == "amharic":

            text = (
                "🚀 ወደ WagaBid እንኳን በደህና መጡ!"
            )

        elif lang == "oromo":

            text = (
                "🚀 Baga gara WagaBid dhuftan!"
            )

        bot.edit_message_caption(
            caption=text,
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=main_menu(lang)
        )


# =========================================================
# BOT START MESSAGE
# =========================================================

print("🤖 WagaBid Bot is running...")


# =========================================================
# KEEP BOT RUNNING FOREVER
# =========================================================

bot.infinity_polling()
