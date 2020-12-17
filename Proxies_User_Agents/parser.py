import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform



def get_html(url, useragent=None, proxy=None ): #НУЖНО ДЛЯ ТОГО ЧТОБЫ ПОЛУЧИТЬ ССЫЛКУ
    print('get_html')
    r = requests.get(url, headers = useragent, proxies=proxy )
    return r.text


def get_ip(html):
    print('New proxy & User-Agent:')
    soup = BeautifulSoup(html, 'lxml')

    ip = soup.find('span', class_="ip").text.strip()# мне нужен только текст его из-зв этого указал text strip очищает от ненужных вещей
    ua = soup.find('span', class_="ip").find_next_sibling('span').text.strip()
    print(ip)
    print(ua)
    print('---------------------')

def main():
    url = 'http://sitespy.ru/my-ip'

    useragents = open('useragents.txt').read().split('\n')#я открываю файл с юзерами потом через read() читаю и через split('\n') исправляю перенос строки
    proxies = open('proxies').read().split('\n')

    for i  in range(10):
        a = uniform(5,8)# нужно для того чтобы компьютер ждал претормозил от скольки до скольки секунд
        sleep(a)
        print(a)


        proxy = {'http': 'http://'+ choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}

        # print(useragent)

        try:
            html = get_html(url, useragent, proxy )
        except:
            continue

        get_ip(html)


if __name__ =='__main__':
    main()
