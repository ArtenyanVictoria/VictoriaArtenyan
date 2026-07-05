import requests
from bs4 import BeautifulSoup
import json
import csv
# r = requests.get(url='https://www.kant.ru/catalog/snowboards/snowboard/')
# if r.status_code == 200:
#     html = r.text.txt
#     with open('snowboards.html', 'w', encoding='utf-8') as f:
#         f.write(html)
with open('snowboards.html', 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
items = soup.find('div', class_='ProductList_products__sDUob').find_all('div', class_='ProductCard_container__CC6VR ProductList_minWidthContainer___v5Jq')

lst = []

for item in items:
    price = item.find('span', class_='ProductCard_price__WxCdM').text

    name = item.find('a', class_='ProductCard_title__AH6iR').text
    print(name)
    d = {'Название': name,
        'Цена': price
    }
    lst.append(d)
# with open('snowboards.json', 'w', encoding='utf-8') as file:
#     json.dump(lst, file, indent=4, ensure_ascii=False)
with open('snowboards.csv', 'w', encoding='utf') as file:
    fieldnames = ["Название", "Цена"]
    writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames)
    writer.writeheader()
    for x in lst:
        writer.writerow(x)



