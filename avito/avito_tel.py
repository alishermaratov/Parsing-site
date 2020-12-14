from selenium import webdriver
from time import sleep
from PIL import Image

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Python\Parsing_saitov\avito\geckodriver')
        self.navigate()#указываем где и куда идти для начала



    def take_screenshot(self):#тут прописали как делать скрин
        self.driver.save_screenshot('avito_screenshot.png')#тут вызываем готовый метод сохронения скриншота


    def crop(self, location, size ):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']


        image.crop((x, y, x+width, y+height)).save('tel.gif')


    def navigate(self):#тут мы начинаем работу с сайтом
        self.driver.get('https://www.avito.ru/moskva/telefony/samsung_galaxy_a50_blue_2049583064')#тут мы указываем какую именно ссылку открывать .get это переход на эу страницу

        button = self.driver.find_element_by_xpath('//button[@class="button-button-2Fo5k button-size-l-3LVJf button-success-1Tf-u width-width-12-2VZLz"]') #тут мы в этом случае находим кнопку и смотрим обозначения find_element_by_xpath это нужно для того чтобы мы смогли находить активные конпки т.д потом находим обозначения конпки batton и находим его класс или отличительную вещь чтобы он понимал и смок кликнуть по ней
        button.click()#сверху мы записали batton все элементы кнопки и уже в этом разделе мы кликае по нему

        sleep(3)

        self.take_screenshot() #тут делваем скрин и получается сверху прописали как

        image = self.driver.find_element_by_xpath('//div[@class="column-root-N_0Ue column-no_width-2PTFn"]//img[@class="contacts-phone-3KtSI"]')
        location = image.location
        size = image.size

        self.crop(location, size )









def main():
    b = Bot()



if __name__ == '__main__':
    main()
