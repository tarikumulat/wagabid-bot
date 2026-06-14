import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


# /start command
@bot.message_handler(commands=['start'])
def start(message):

    bot.send_photo(
        message.chat.id,
        photo=open("logo.png", "rb"),
        caption="🚀 Welcome to WagaBid!"
    )


print("🤖 Bot is running...")

bot.infinity_polling()
