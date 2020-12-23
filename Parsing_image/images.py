import requests
import os

#---------------это просто скачать одну фотку самый простой вариант
# url = 'https://www.hdwallpapers.in/thumbs/2020/trees_on_rocks_above_body_of_water_hd_nature-t2.jpg'#это урл картинки самой
#
# r = requests.get(url, stream=True)#открываем эту ссылку и на чтения get пишем #stream нужен для того чтобы парсить кусками ведь мы не знаем сколько там весит а это все будет нагружать оперативную память
#
# with open('1.jpg', 'bw') as f: #тут мы открываем и пишем имя файла, потом через as присваеваем открытый уже файл на переменную f# bw означает читай файл если w то это текстовый файл
#     for chunk in r.iter_content(8192): #нам нужно вывести в маем случае фотку и через iter_content() мы соединяем все куски это функция request-а на контент указывем сколько килобайт будем делить или по сколько килобайт будем вытаскивать
#         f.write(chunk) #потом на чтения мы передаем файл chang  потомучто в этом файле все будет хранится

urls = [
    'https://www.hdwallpapers.in/thumbs/2020/large_height_green_trees_reflection_on_buttermere_lake_and_landscape_of_sand_covered_mountain_hd_nature-t2.jpg',
    'https://www.hdwallpapers.in/thumbs/2020/lake_with_leaves_between_green_grass_covered_forest_with_reflection_during_daytime_hd_nature-t2.jpg',
    'https://www.hdwallpapers.in/thumbs/2020/clear_view_of_under_body_of_water_in_florida_keys_4k_hd_nature-t2.jpg',
    'https://www.hdwallpapers.in/thumbs/2020/blue_yellow_body_of_water_between_sand_covered_mountains_and_forest_under_cloudy_blue_sky_hd_nature-t2.jpg',
    'https://www.hdwallpapers.in/thumbs/2020/beautiful_pathway_between_fence_and_garden_and_body_of_water_with_sunrays_hd_nature-t2.jpg'
]

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


def main():
    for url in urls:#тут мы проводим через цикл так как у нас несколько ссылрк несколько фото чтобы каждую сканировал мы это делаем
        save_image(get_name(url), get_file(url))#тут так как мы указали в функции  save_image нужно имя и сам файл имя мы дастоем в функции get_name(url) а вот сам файл возвращает функция get_file(url):

if __name__ == '__main__':
    main()
