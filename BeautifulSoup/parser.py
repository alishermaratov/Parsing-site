from bs4 import BeautifulSoup
import re


regexp = r'\d{2}.\d{2}.\d{4}'#это делается для того чтобы мы записали все как есть все значения записались тут мы записываем дату




def main():
    html = open('index.html').read()
    soup = BeautifulSoup(html, 'lxml')

    # div = soup.find('div', class_='links')
    # links =div.find_all('a', {'class': 'links'})
    text = soup.find('h1').next_element#next_element это элемент после обозначения пример после  стоит слово heder его и вывели так как он следующий можно указывать несколько раз и некст некст показывает дальше дальше
    text = soup.find('h1').next_element.next_element.next_element
    #можно просто
    text = soup.find('h1').next
    #или можно
    text = soup.find('h1').next_subling#это уже с тегом следующую информацию вытаскивать
    text = soup.find('h1').previous_subling#это некст снизу вверх берет вверхний элемент
    a = soup.find('a', href=re.compile('ya.ru'))
    a = a.get('href')#через гет можем извелкать саму ссылку саму информацию
    div = soup.find('h1').parent#parent будет искать большой класс родителей этого значения и уже оттуда берем обозначения
    n = div.get('data-set')#тут мы получаем значения дива сверху который родительского класса потпм из этого родителя серез гет достаем значения дата сет а
    a = soup.find('a', href=re.compile('bing.com$'))#знак доллара обозначает что мы ищем именно эту ссылку и не другие что дальше мы не ждем нисего другого
    a = soup.find('a', href=re.compile('2'))#тут мы ищем ссылку в котором есть цифра 2 и он нам будет искать ссылки в обозначение а цифру 2 и первую ссылку которую нашел выводит
    a1 = soup.find('a', text=re.compile('post'))#если я хочуу найти что то по тексту именно по названию или по кнопке то тут указываем что он текстовый фацл
    a = soup.find('div', text=re.compile(regexp))
    print(a1)




if __name__=='__main__':
    main()
