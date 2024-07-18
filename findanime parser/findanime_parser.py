from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import pprint
import pickle

DOMEN ='https://findanime.net'
url = 'https://findanime.net/list'
params = {'offset': 0}                                                                   # Цикл будет перебираться по 50 штук за раз (сейчас максимум до 8350)
titles_count = 500                                                                       # Переменная для количетсва обрабатываемых тайтлов
names = []
links = []
descriptions = []


for i in range(params['offset'], titles_count, 50):

    html = requests.get(url, headers={'User-Agent': UserAgent().chrome}, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')

    # Получение названий и ссылок

    h_tags = soup.find_all('h3')
    for h in h_tags:
        text = h.find('a')
        names.append(text.get('title'))
        links.append(DOMEN + text.get('href'))



    descs = soup.find_all('div', 'manga-description')
    for desc in descs:
        descriptions.append(desc.text.replace('\n',''))

    params['offset'] += 50
    count = params['offset']
    print(f'Обработано тайтлов: {count}')

info = list(zip(names, descriptions, links))
# pprint.pprint(info)

with open('report.txt', mode='wb') as f:
    pickle.dump(info, f)
