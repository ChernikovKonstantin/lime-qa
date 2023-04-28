import os
import time
import re

import allure
from selene.api import be, have, s
from selene.support.shared.jquery_style import ss

from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.login import LoginPage


class SmokePage(BasePage):
    # locators main page
    banners_main_image = ss("//div[@class = 'slide' and @style != 'cursor: pointer;']")
    video_main_image = s("//video")
    block_icon_string = "//div[@class='App isHomepage page-index isAppNotify isEmptyCart']"
    first_catalog_image = s("(//picture/img)[1]")
    first_catalog_video = s("(//video[@class='d-none d-md-block'])[1]")
    first_catalog_video_attribute = s("(//video[@class='d-none d-md-block'])[1]//child::*")

    # locators button

    button_search = s("//button[@class='SearchBox__button']")





    card_number_field = s("//input[@type='text' and @placeholder='Введите номер карты']")
    validity_period_field = s("//input[@type='text' and @placeholder='Дата окончания срока действия']")
    card_holder_field = s("//input[@type='text' and @placeholder='Владелец карты']")
    security_code_field = s("//input[@type='text' and @placeholder='Код безопасности CVV2']")
    promo_code_field = s("//input[@type='text' and @placeholder='Промокод']")
    to_pay_btn = s("//button[@class ='btn btn-block']")
    to_pay_btn_string = "//button[@class ='btn btn-block']"
    success_btn = s("//button[@class = 'button button_primary']")
    success_btn_string = "//button[@class = 'button button_primary']"
    success_btn_fault = s("//button[@class='button button_secondary']")
    success_btn_fault_string = "//button[@class='button button_secondary']"


    @allure.step('Цикл проверки баннеров')
    def cycle_banners(self):

        for i in range(len(self.banners_main_image)):
            list_first_attribute_banners = ['https://cache-limeshop.cdnvideo.ru/limeshop/aa/734083954af8f1a65bf3a11ed9d9900155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/73344231819676f30b73f11ed9d9600155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/73164154295cc9644a39611ed9d8f00155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/73107092616306c58bff011ec9d3700155d011401.jpeg?q=85&w=440',
                                            '']
            url_main = self.get_url()
            self.click(self.banners_main_image[i], " баннер")
            first_image = self.get_attribute(self.first_catalog_image, "data-src")
            self.assert_check_expressions(list_first_attribute_banners[i], first_image, " некорректное отображение порядка товаров в каталоге")
            self.open_url(os.getenv('base_url'))
            #self.driver.back() поправить на возврат назад
            url_main_return = self.get_url()
            time.sleep(2)
            self.wait_element(self.block_icon_string) #ожидание блока иконок белого цвета
            self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")



    @allure.step('Проверка видео')
    def video(self):

        video = 'https://cache-limeshop.cdnvideo.ru/limeshop/landing-pages/summer-basic-23/01_desc+ipad.mp4'
        url_main = self.get_url()
        self.click(self.video_main_image, " видео")
        first_video = self.get_attribute(self.first_catalog_video_attribute, "src")
        self.assert_check_expressions(video, first_video,
                                      " некорректное отображение видео в каталоге")
        first_video_loop = self.get_attribute(self.first_catalog_video, "loop")
        self.assert_check_expressions("true", first_video_loop,
                                      " нет тега автовоспроизведения видео")
        self.open_url(os.getenv('base_url'))
        url_main_return = self.get_url()
        self.wait_element(self.block_icon_string)  # ожидание блока иконок белого цвета
        self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")











