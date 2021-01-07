import requests
from bs4 import BeautifulSoup
from lxml import *
import csv

# план
# 1 количество страниц
# 2 сформировать список урлов на страницы выдачи
# 3 собрать данные

def get_html(url):
    r = requests.get(url)
    return r.text

#узнаем количество страницы
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages clearfix').find_all('a', class_='pagination-page')[-1].get('href')#тут мы для начала soup принимаетобьект html и в нем ищет  find ищет где менно искать первая попавшися html строке а find_all ищет уже в строках которых выделил find ему тут пишутся какаой он имеет обозначения и где искать а вот find all ищет определенные вещи которые ты сам ему прописываешь несколько парсить и у них пишешь что то общее [--------1] это какой именнр файл выдялить можно было все но тут ищем последнюю

    total_pages = pages.split('=')[1].split('&')[0] #тут уже нам нужно достать именно номер страницы мы делим и помещяем массив делим по знакам или определенным буквам до тех пор пока не достанем свою информацию

    return int(total_pages)#функция возвращает количество страницы

def write_csv(data):
    with open('avito.csv', 'a',) as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')

        writer.writerow((data['title'],
                          data['price'],
                          data['metro'],
                          data['url']))



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div',class_="items-items-38oUm").find_all('div', class_="iva-item-root-G3n7v photo-slider-slider-15LoY iva-item-list-2_PpT items-item-1Hoqq items-listItem-11orH js-catalog-item-enum")

    for ad in ads:
        # title, price, metro, url
        name = ad.find('div', class_='iva-item-body-NPl6W').find('div', class_='iva-item-titleStep-2bjuh').text.strip().lower()


        if 'samsung' in name:

            try:
                title = ad.find('div', class_='iva-item-body-NPl6W').find('div', class_='iva-item-titleStep-2bjuh').text.strip()
            except:
                title = ''

            try:
                url = 'https://www.avito.ru' + ad.find('div', class_='iva-item-body-NPl6W').find('div', class_='iva-item-titleStep-2bjuh').find('a').get('href')
            except:
                url = ''

            try:
                price = ad.find('div', class_='iva-item-priceStep-2qRpg').find('meta', itemprop ="price").get('content').text.strip()
            except:
                price = ''

            try:
                metro = ad.find('div', class_='geo-root-1pUZ8 iva-item-geo-1Ocpg').find_all('span')[1].text.strip()
            except:
                metro = ''

            data = {'title': title,
                    'price': price,
                    'metro': metro,
                    'url': url}

            write_csv(data)
        else:
            continue

def main():
    url = 'https://www.avito.ru/moskva/telefony/samsung-ASgBAgICAUSeAugJ?p=1&q=samsung'
    base_url = 'https://www.avito.ru/moskva/telefony/samsung-ASgBAgICAUSeAugJ?'
    page_part = 'p='
    query_part = '&q=samsung'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, 5):
        url_gen = base_url + page_part + str(i) + query_part
        # print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)



if __name__ == '__main__':
    main()
