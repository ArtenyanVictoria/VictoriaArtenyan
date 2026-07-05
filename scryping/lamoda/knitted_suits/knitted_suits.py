from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
import csv
# driver = webdriver.Chrome()
# for i in range(1, 6):
#     driver.get('https://www.lamoda.ru/c/7571/default-knitted-suits/?page=' + str(i))
#
#     time.sleep(10)
#     with open('page_of_knitted_suits/knitted_suits' + str(i) + '.html', 'w', encoding='utf-8') as file:
#         file.write(driver.page_source)
#
#
# driver.quit()

lst = []
for i in range(1, 6):
    with open('page_of_knitted_suits/knitted_suits' + str(i) + '.html', 'r', encoding='utf-8') as file:
        html = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='grid__catalog').find_all('div', class_='x-product-card__card x-product-card__card_catalog')
    for item in items:
        name = item.find('div', class_='x-product-card-description__brand-name _brandName_1rcja_6').text + ' (' + item.find('div', class_='x-product-card-description__product-name _productName_1rcja_7').text + ')'
        price = item.find('div', class_='x-product-card-description__microdata-wrap x-product-card-description__price-wrap').find('span').text
        link = 'https://www.lamoda.ru' + item.find('a', class_='_root_f9xmk_2 _label_f9xmk_20 x-product-card__pic x-product-card__pic-catalog x-product-card__pic x-product-card__pic-catalog')['href']

        d = {'Название': name, 'Цена': price, 'ссылка': link}
        lst.append(d)
# with open('knitted_suits.json', 'w', encoding='utf=8') as file:
#     json.dump(lst, file, indent= 4, ensure_ascii= False)
# with open('knitted_suits.csv', 'w', encoding='utf=8') as f:
#     fieldnames = list(lst[0].keys())
#     writer = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames)
#     writer.writeheader()
#     for i in range(len(lst)):
#         writer.writerow(lst[i])










