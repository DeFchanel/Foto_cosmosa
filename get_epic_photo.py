import requests
import os
import datetime
from dotenv import load_dotenv
from download_img import download_img



def get_epic_photo(nasa_token):
    payload_epic = {
        'api_key': nasa_token
    }
    response_epic = requests.get('https://api.nasa.gov/EPIC/api/natural', params=payload_epic)
    response_epic.raise_for_status()
    epic_response_content = response_epic.json()
    for number, image in enumerate(epic_response_content):
        filename = f'nasa_epic_{number}.png'
        file_path = os.path.join(dir_name, filename)
        image_name = epic_response_content[number]['image']
        image_date1 = epic_response_content[number]['date']
        image_date = datetime.datetime.fromisoformat(image_date1)
        formatted_image_date = image_date.strftime("%Y/%m/%d")
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_image_date}/png/{image_name}.png'
        download_img(file_path, epic_url, params=payload_epic)


if __name__ == '__main__':
    load_dotenv()
    dir_name = 'images'
    os.makedirs(dir_name, exist_ok=True)
    nasa_token = os.getenv('NASA_TOKEN')
    get_epic_photo(nasa_token)