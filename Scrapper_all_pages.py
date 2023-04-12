import bs4
import requests

# пошук в заданій зоні
url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page='

map = {}

id = 0

# максимальна кількість сторінок
max_pages = 20

for p in range(max_pages):                       #Проходимо всі сторінки, щоб зчитати

    cur_url = url + str(p + 1)

    print("Скрапінг сторінки №: %d" % (p + 1))

    html_text = requests.get(cur_url).text       #Робимо запит і отримуємо html відповідної сторінки
    soup = bs4.BeautifulSoup(html_text, 'lxml')  #Використовуємо парсер lxml

    ads = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')   #Знаходимо всі рядки товару

    for i in range(len(ads)):

        ad = ads[i]
        id += 1
        map[id] = {}

        name = ad.find('a', class_='title').text
        price = ad.find('h4', class_='pull-right price').text
        description = ad.find('p', class_='description').text
        map[id]["name"] = name
        map[id]["price"] = price
        map[id]["description"] = description
print(map)
