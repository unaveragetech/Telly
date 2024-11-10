import os
import json
import telebot
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing from the .env file")

# Load bot configuration
with open("bot_config.json") as config_file:
    config = json.load(config_file)

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Load triggers and responses
with open("responses.json") as responses_file:
    responses = json.load(responses_file)

# Define greeting and general response handlers
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi there. What’s happening?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    response = responses.get(message.text.lower(), message.text)  # Default to echo if no specific response
    bot.reply_to(message, response)

# Start polling
if config.get("infinity_polling", True):
    bot.infinity_polling()
else:
    bot.polling()
