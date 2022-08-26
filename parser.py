import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://minfin.com.ua/'
URL = 'https://minfin.com.ua/ua/cards/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='sc-182gfyr-0 jmBHNg')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='be80pr-15 kwXsZB').find('a', class_='cpshbz-0 eRamNS').get('alt'),
                'link_product': item.find('div', class_='be80pr-15 kwXsZB').find('a').get('href'),
                'brand': item.find('div', class_='be80pr-16 be80pr-17 kpDSWu cxzlon').find('span', class_='be80pr-21 dksWIi').get_text(),
                'card_img': item.find('div', class_='be80pr-9 fJFiLL').find('img').get('src')
            }
        )
    return cards


def save_doc(items, path):
    with open(path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['назва продукту', 'посилання на продукт', 'банк', 'зоображення на картинку'])
        for item in items:
            writer.writerow([item['title'], item['link_product'], item['brand'], item['card_img']])


def parser():
    # якщо парсимо сайт з декількома сторінками, то
    # PAGENATION = input('вкажіть кількість сторінок для парсингу: ')
    # PAGENATION = int(PAGENATION).strip()

    html = get_html(URL)
    if html.status_code == 200:
        cards = get_content(get_html(URL).text)
        # якщо парсимо сайт з декількома сторінками, то
        # cards = []
        # for page in range(1,PAGENATION):
        #     print(f'Парсим сторінку: {page}')
        #     html = get_html(URL, params={'page': page})
        #     cards.extend(get_content(html.text))
        # print(cards)
        save_doc(cards, CSV)
    else:
        print("Error")


parser()
