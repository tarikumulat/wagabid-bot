import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


# /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🚀 WagaBid Bot is online!"
    )


print("🤖 Bot is running...")

bot.infinity_polling()
