from download_img import download_img
import requests
import os
import argparse



def fetch_spacex_last_launch():
    response1 = requests.get(f'https://api.spacexdata.com/v5/launches/{spacex_launch_id}')
    response1.raise_for_status
    links = (response1.json()['links']['flickr']['original'])
    for link_number, link in enumerate(links):
        filename = f'spacex_{link_number}.jpeg'
        file_path = os.path.join(dir_name, filename)
        download_img(file_path, link)

if __name__ == '__main__':
    dir_name = 'images'
    os.makedirs(dir_name, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Программа скачивает фото Spacex по указанному вами ID запуска'
    )
    parser.add_argument('id', help='ID запуска')
    args = parser.parse_args()
    spacex_launch_id = args.id
    fetch_spacex_last_launch()