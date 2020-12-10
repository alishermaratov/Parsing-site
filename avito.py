import requests
from bs4 import BeautifulSoup
from lxml import *

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

def main():
    url = 'https://www.avito.ru/moskva/telefony/samsung-ASgBAgICAUSeAugJ?p=1&q=samsung'
    base_url = 'https://www.avito.ru/moskva/telefony/samsung-ASgBAgICAUSeAugJ?'
    page_part = 'p='
    query_part = '&q=samsung'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages ):
        url_gen = base_url + page_part + str(i) + query_part
        print(url_gen)



if __name__ == '__main__':
    main()
