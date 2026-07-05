import random
import requests

from bs4 import BeautifulSoup
import time
import json
import csv


# for i in range(1, 6):
#     r = requests.get(url='https://copterdrone.ru/catalog/rc_planes/?page=' + str(i) + '&page=' + str(i))
#     if r.status_code == 200:
#         html = r.text.txt
#         with open('planes/p' + str(i) + '.html', 'w', encoding='utf-8') as file:
#             file.write(html)
#             time.sleep(random.randint(1, 3))
#             print('скачена ' + str(i) + ' из ' +  str(5) +  ' страниц')
lst = []
for i in range(1, 6):
    with open('planes/p' + str(i) + '.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='cats-products__wrap').find_all('div', class_='cats-good-card goodCard swiper-slide')
    for item in items:
        name = item.find('a', class_='goodTitle').text
        price = item.find('span', class_='cats-good-card__price--new goodPrice').text
        description = item.find('p', class_='week-sale-slider__text-n').text.strip()
        link_plane = 'https://copterdrone.ru' + item.find('a', class_='cats-good-card__img goodImg')['href']
        link_picture = 'https://copterdrone.ru' + item.find('img')['src']
        d = {'Название': name,
             'Цена': price,
             'Описание': description,
             'Ссылка на самолетик': link_plane,
             'Ссылка на картинку': link_picture}
        lst.append(d)



lst = sorted(lst, key= lambda item: int(item['Цена'].split()[0]))
with open('planes.json', 'w', encoding='utf-8') as f:
    json.dump(lst, f, indent=4, ensure_ascii=False)
with open('planes.csv', 'w', encoding='utf-8') as file:
    fieldnames = list(lst[0].keys())
    writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames)
    writer.writeheader()
    for x in lst:
        print(x)
        writer.writerow(x)










