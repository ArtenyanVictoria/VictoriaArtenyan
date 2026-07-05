from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import csv
import json
if not os.path.exists('data'):
    os.mkdir('data')
driver = webdriver.Chrome()
driver.get('https://akademkukol.ru/product-category/konf/')
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
li_s = soup.find('ul', class_='products columns-4').find_all('li')
for li in li_s:
    link = li.find('a')['href']
    driver.get(link)
    print(link)
    name_file = str(link).split('/')[-2]
    with open(f'data/{name_file}.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)

driver.quit()

lst_data_files = os.listdir('data')
print(lst_data_files)
lst = []
for i in range(len(lst_data_files)):
    with open('data/' + str(lst_data_files[i]), 'r', encoding='utf=8') as file:
        html = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('ul', class_='products columns-4').find_all('span', class_='nxowoo-box')
    for item in items:
        name = item.find('h2', class_='woocommerce-loop-product__title').text
        price = str(item.find('span', class_='woocommerce-Price-amount amount').text).replace(' ', ' ')
        link = item.find('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')['href']
        print(price)
        d = {'Название': name,
             'Цена': price,
             'ссылка': link
             }
        lst.append(d)

with open('dolls.json', 'w', encoding='utf=8') as file:
    json.dump(lst, file, indent=4, ensure_ascii=False)
with open('dolls.csv', 'w', encoding='utf=8') as f:
    fieldnames = list(lst[0].keys())
    writer = csv.DictWriter(f, delimiter=";", fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lst)):
        writer.writerow(lst[i])













