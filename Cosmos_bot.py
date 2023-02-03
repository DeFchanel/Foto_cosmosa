import telegram
import os
from dotenv import load_dotenv
import time
import argparse


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    bot = telegram.Bot(token=telegram_bot_token)
    parser = argparse.ArgumentParser(
    description='Программа высылает фото в Telegram канале c указанной вами задержкой'
    )
    parser.add_argument('--delay', help='Задержка', default=14400)
    args = parser.parse_args()
    posting_period = args.delay
    while True:
        for root, dirs, files in os.walk("images"):
            for filename in files:
                image_path = os.path.join(root, filename)
                with open(image_path, "rb") as file:
                    photo = file.read()
                    bot.send_photo(chat_id=chat_id, photo=photo)
                time.sleep(float(posting_period))