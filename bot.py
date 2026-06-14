
import telebot

# 🔑 Put your NEW token here (from BotFather)


# replaced TOKEN = "8739754370:AAE4Ub5Vxtm5inv_7geUc40n1soxEpwa2H4"

import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


# ---------------------------
# /start command
# ---------------------------
@bot.message_handler(commands=['start'])
def start(message):
    print('Start received')
    
    bot.send_photo(
        message.chat.id,
        photo=open("logo.png", "rb"),
        #caption="Welcome to WagaBid 🔄\nReverse Auction Platform"
    )
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🟢 Buy")
    markup.row("🔴 Sell")

    bot.send_message(
        message.chat.id,
        "Welcome to WagaBid 🔄\n\n"
        "Do you want to Buy or Sell?",
        reply_markup=markup
    )
    
    


# ---------------------------
# Handle Buy/Sell buttons
# ---------------------------
@bot.message_handler(func=lambda message: True)
def handle(message):
    text = message.text

    if text == "🟢 Buy":
        bot.send_message(
            message.chat.id,
            "You selected BUY 🟢\n\n"
            "Next step: use /new to create a reverse auction request."
        )

    elif text == "🔴 Sell":
        bot.send_message(
            message.chat.id,
            "You selected SELL 🔴\n\n"
            "Next step: use /bid to place offers in auctions."
        )

    else:
        bot.send_message(
            message.chat.id,
            "Please use the buttons: 🟢 Buy or 🔴 Sell"
        )


# ---------------------------
# Run bot
# ---------------------------
print("🤖 Bot is running...")
bot.infinity_polling()
