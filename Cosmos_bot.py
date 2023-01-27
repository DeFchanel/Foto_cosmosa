import telegram
import os
from dotenv import load_dotenv
load_dotenv()


telegram_bot_token = os.getenv('TELEGRAM_TOKEN')
chat_id = '@foto_cosmosa'

bot = telegram.Bot(token=telegram_bot_token)
with open('./images/nasa_epic_1.png', 'rb') as photo:
    bot.send_photo(chat_id, photo=photo)