import requests
from bs4 import BeautifulSoup
from lxml import *
import os


def get_html(url):
    # print("5dd55d5d")
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='paginator clearfix').find_all('li')[9]#тут мы для начала soup принимаетобьект html и в нем ищет  find ищет где менно искать первая попавшися html строке а find_all ищет уже в строках которых выделил find ему тут пишутся какаой он имеет обозначения и где искать а вот find all ищет определенные вещи которые ты сам ему прописываешь несколько парсить и у них пишешь что то общее [--------1] это какой именнр файл выдялить можно было все но тут ищем последнюю
    pages2 = pages.find('a').get('href')
    total_pages = pages2.split('=')[1]

    return int(total_pages)

def parsing_href(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div',id="results").find_all('div', class_="row vw-item list-item yellow a-elem")
    a=[]
    for ad in ads:
        nnn = ad.find('div', class_='a-elem__picture').find('img').get('src')
        a.append(nnn)

    return a

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div',id="results").find_all('div', class_="row vw-item list-item yellow a-elem")


    for ad in ads:
        name = ad.find('div', class_='a-info-top').find('a', class_='list-link ddl_product_link').text.strip()
        return name

def get_file(url):
    r = requests.get(url, stream=True)
    return r

def get_name(url):
    name = url.split('/')[-1]#split нужен для того чтобы взять имя он делит на определенные вещи на данный момент как мы указали на / там вытаскиваем имя так как нужен последниий индекс так как мы ставим имя через него мы указываем через [-1]
    folder= name.split('.')[0]#тут мы ставим имя и создаем или если есть уже папка туда уже скачиваем спарсинные фотки

    if not os.path.exists(folder):#тут проверяет есть ли папка с таким именем или нет
        os.makedirs(folder)#если той папки нет то просто создаем эту папку
    path = os.path.abspath(folder)#это чтобы мы нашли сразу путь к этой папке указывает абсалютный путь
    return path + '/' + name # / указали для того что там в абсалютном пути его нет и это нужно чтобы этот файл вставился в ту папку

def save_image(name, file_object):
    with open (name, 'bw') as f: #тут вместо name можнл поставить определенное имя но мы тут поставили имя так как будем генерировать имя сами с ссылок
        for chunk in file_object.iter_content(8192):
            f.write(chunk)





def parsim_foto():
    url1= 'https://kolesa.kz/cars/kia/'
    urls = parsing_href(get_html(url1))
    for url in urls:#тут мы проводим через цикл так как у нас несколько ссылрк несколько фото чтобы каждую сканировал мы это делаем
        save_image(get_name(url), get_file(url))

def main():
    parsim_foto()
    url = 'https://kolesa.kz/cars/kia/?page=1'
    base_url = 'https://kolesa.kz/cars/kia/?'
    page_part = 'page='


    total_pages = get_total_pages(get_html(url))

    for i in range(1, 5):
        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen)
        get_page_data(html)





if __name__ == '__main__':
    main()
