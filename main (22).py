# https://copterdrone.ru/catalog/rc_cars/
import requests
from bs4 import BeautifulSoup
import csv
import json
# r = requests.get(url='https://copterdrone.ru/catalog/rc_cars/')
# if r.status_code == 200:
#     html = r.text.txt
#     with open ('fille.html', 'w') as f:
#         f.write(html)
# print(html)

lst = []
with open('fille.html', 'r') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
res = soup.find('div', class_='cats-products__wrap').find_all('div', class_='cats-good-card goodCard swiper-slide')
for item in res:
    name = item.find('a', class_='goodTitle').text
    price = item.find('span', class_='cats-good-card__price--new goodPrice').text
    link = 'https://copterdrone.ru' + item.find('a', class_='cats-good-card__img goodImg')['href']
    link_picture = 'https://copterdrone.ru' + item.find('img')['src']
    d = {'Название': name,
         'Цена': price,
         'Ссылка на машину': link,
         'Ссылка на картинку': link_picture}
    lst.append(d)
# with open("filee.json", 'w') as f:
#     json.dump(lst, f, indent=4, ensure_ascii=False)
with open('filee.csv', 'w') as file:
    fieldnames = ['Название','Цена', 'Ссылка на машину', 'Ссылка на картинку']
    writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames)
    writer.writeheader()
    for x in lst:
        writer.writerow(x)





# https://copterdrone.ru/catalog/rc_cars/huangbo/radioupravlyaemaya-mashina-dlya-drifta-hb-ford-mustang-4wd-svet-par-akb-116-sc16a01-1/
# /catalog/rc_cars/huangbo/radioupravlyaemaya-mashina-dlya-drifta-hb-ford-mustang-4wd-svet-par-akb-116-sc16a01-1/


