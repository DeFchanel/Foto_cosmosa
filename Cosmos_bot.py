import telegram
import os
from dotenv import load_dotenv
load_dotenv()


telegram_bot_token = os.getenv('TELEGRAM_TOKEN')
chat_id = '@foto_cosmosa'

bot = telegram.Bot(token=telegram_bot_token)
bot.send_message(chat_id=chat_id, text="Hello Telegram")
