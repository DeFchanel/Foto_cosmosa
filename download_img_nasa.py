from download_img import download_img
from dotenv import load_dotenv
import requests
import os
from urllib.parse import urlparse
load_dotenv()


dir_name = 'images'
os.makedirs(dir_name, exist_ok=True)
nasa_token = os.getenv('NASA_TOKEN')


def get_file_extension(parse_path):
    extension = os.path.splitext(parse_path)
    return extension[1]


def download_img_nasa():
    count = 30
    payload = {
    'api_key': nasa_token,
    'count': count
    }
    nasa_response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    nasa_response.raise_for_status
    links = nasa_response.json()
    for number, image in enumerate(links):
        if image['media_type'] == 'video':
            continue
        nasa_photo_url = image['url']
        parse = urlparse(nasa_photo_url)
        parse_path = parse.path
        extension = get_file_extension(parse_path)
        filename = f'nasa_apod_{number}.{extension}'
        file_path = os.path.join(dir_name, filename)
        download_img(file_path, nasa_photo_url)

download_img_nasa()