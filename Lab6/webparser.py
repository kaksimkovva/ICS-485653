from bs4 import BeautifulSoup
import requests
import numpy as np


def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    for link in soup.find_all('a', href=True):
        href_array = np.array(link['href'])
        if np.char.startswith(href_array, 'http', start=0, end=None):
            print(href_array)


def get_images_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    # Print images alt
    print("\n".join([img['alt'] for img in soup.find_all('img', alt=True)]))
    print(f'Images count: {len(soup.find_all("img"))}')


get_images_count('https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html')
get_all_links('https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html')