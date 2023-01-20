import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
from pprint import pprint
import datetime
load_dotenv()


count = 30
dir_name = 'images'
filename = 'hubble.jpeg'
filename2 = 'pop.jpeg'
nasa_token = os.getenv('NASA_TOKEN')
file_path = os.path.join(dir_name, filename)
os.makedirs(dir_name, exist_ok=True)
payload = {
    'api_key': nasa_token,
    'count': count
}
payload_epic = {
    'api_key': nasa_token
}
#url = input()
url_spacex = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
nasa_url = 'https://api.nasa.gov/planetary/apod'
url_epic = 'https://api.nasa.gov/EPIC/api/natural'


def download_img(file_path, url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url_spacex):
    response1 = requests.get(url)
    response1.raise_for_status
    links = (response1.json()['links']['flickr']['original'])
    for link_number, link in enumerate(links):
        filename = f'spacex_{link_number}.jpeg'
        file_path = os.path.join(dir_name, filename)
        download_img(file_path, link)


def download_img_nasa(url):
    nasa_response = requests.get(url, params=payload)
    nasa_response.raise_for_status
    links = nasa_response.json()
    for link in range(count):
        nasa_photo_url = links[link]['hdurl']
        parse = urlparse(nasa_photo_url)
        parse_path = parse.path
        extension = get_file_extension(parse_path)
        filename = f'nasa_apod_{link}.{extension}'
        file_path = os.path.join(dir_name, filename)
        download_img(file_path, nasa_photo_url)


def get_file_extension(parse_path):
    extension = os.path.splitext(parse_path)
    return extension[1]


def get_epic_photo(url_epic):
    response = requests.get(url_epic, params=payload_epic)
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


fetch_spacex_last_launch(url_spacex)
#get_epic_photo(url_epic)