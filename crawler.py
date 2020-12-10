

# 1.парсер однопоточный
# 2.замер времени
# 3.multiprocessing pool
# 4. замер времени
# 5, экспорт данных в ссв файл


import requests
# requests БУДЕТ ПОЛУЧАТЬ HTML КОД КАЖДОЙ СТРАНИЦЫ
from bs4 import BeautifulSoup
from lxml import *
import csv
from datetime import datetime
import time
from multiprocessing import Pool





def get_html(url):#откуда парсить принимает
    r = requests.get(url)#эта функция будет получать значения юрл ссылко с помощью requests функцияй get,и этот  get получает в качестве аргументов ссылку
    return r.text #возвращает html код той страницы которая передана в (url)



def get_all_links(html): #ота будет принимать все страницы от html
    soup = BeautifulSoup(html, 'lxml')#передали значения это код html и указания на парсер который будет использоватся

    tds = soup.find('tbody').find_all('tr', class_ = 'cmc-table-row')#тут мы первый находим таблицу прописываем под каким классом он находится потом мы в этой же таблице ищем посты через класс или стайл его(особенный примечания в этом коде)
    #в tds мы находим нам нужные ссылкий

    links = []# сюда записываем спарсенные ссылки
#td это в коде сайта в тд записываются главные вещи вот что это
    for td in tds: #для каждого тд в списке сверху тдс будем делать следующее
        a = td.find('a').get('href')#здась мы в 'a' это до главной ссылки находится и в этом пукте мы забираем главную ссылку на эту через get в 'href'
        link = 'https://coinmarketcap.com/' + a#это сделано для того чтобы когда выводился сайт пред ним стояла уже готовая ссылка
        links.append(link)#через аппенд мы добавляем те самые ссылки котрые нашли и у нас появляется целый спиок линкс с ссылками

    return links



def get_page_data(html):#тут мы уже из готовых ссылок которых мы достали достаем названия и цену с этих страниц
    soup = BeautifulSoup(html, 'lxml')#для парсинга нужная вещь

    try:#try:except: это для того если у меня не сработает то что написал не найдется то сработает второе
        name= soup.find('h1').text.strip()#тут мы берем имя и с помощью text переводим строку и с помощью strip мы убираем лишнее
    except:
        name = ''
    try:
        price = soup.find('span', class_='cmc-details-panel-price__price').text.strip()#тут мы берем цену и с помощью text переводим строку и с помощью strip мы убираем лишнее
    except:
        price = ''

    data = {'name' : name,
            'price' : price}#загоняем значения в библиотеку чтобы вытаскивать данные
    return data

def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:#with нужен для того чтобы полюбому выполнять это все
        writer = csv.writer(f)#для записи данных с запятыми

        writer.writerow ((data['name'],
                          data['price']))#чтобы брать информацию и записывать
        print(data['name'], 'parsed')

def make_all(url):#это чисто для того чтобы передавать и вытащить информацию с страницы снизу уже через процесс это все запускается и работает
    html = get_html(url)#первый передаем url
    data = get_page_data(html)#потом готовый html мы пердаем на следующую функцию
    time.sleep(5)
    write_csv(data)#потом в этой функции записываем результат



def main():
    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all/'
    all_links = get_all_links(get_html(url))#все ссылки из которых мы будем доставать ссылки на парсинг

    # for index, url in enumerate(all_links):#индекс это номерацию ставим через  enumerate
    #
    #     html = get_html(url)#первый передаем url
    #     data = get_page_data(html)#потом готовый html мы пердаем на следующую функцию
    #     write_csv(data)#потом в этой функции записываем результат
    #     print(index+1)
    #     time.sleep(5)



    with Pool(40) as p:#это нужно для того чтобы через несколько процессов парсить
        p.map(make_all, all_links)#тут мы передаем переменные и функии сверху

    end = datetime.now()

    total = end - start

    print(str(total))





if __name__ =='__main__':
    main()

# print(get_all_links(get_html('https://coinmarketcap.com/')))
