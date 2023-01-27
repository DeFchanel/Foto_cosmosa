import requests
import os
import datetime
from dotenv import load_dotenv
from download_img import download_img
load_dotenv()


dir_name = 'images'
os.makedirs(dir_name, exist_ok=True)
nasa_token = os.getenv('NASA_TOKEN')


def get_epic_photo():
    payload_epic = {
        'api_key': nasa_token
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=payload_epic)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filename = f'nasa_epic_{number}.png'
        file_path = os.path.join(dir_name, filename)
        image_name = response.json()[number]['image']
        image_date1 = response.json()[number]['date']
        image_date = datetime.datetime.fromisoformat(image_date1)
        formatted_image_date = image_date.strftime("%Y/%m/%d")
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_image_date}/png/{image_name}.png'
        download_img(file_path, epic_url, params=payload_epic)

get_epic_photo()