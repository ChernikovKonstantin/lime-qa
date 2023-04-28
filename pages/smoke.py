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
from selene.api import browser

class SmokePage(BasePage):
    # locators main page
    banners_main_image = ss("//div[@class = 'slide' and @style != 'cursor: pointer;']")
    video_main_image = s("//video")
    block_icon_string = "//div[@class='App isHomepage page-index isAppNotify isEmptyCart']"
    first_catalog_image = s("(//picture/img)[1]")
    first_catalog_video = s("(//video[@class='d-none d-md-block'])[1]")
    first_catalog_video_attribute = s("(//video[@class='d-none d-md-block'])[1]//child::*")
    #interesnaia_construkciya = s(//span[contains(@class,"mainmenu__link has-children")])

    # locators button

    batton_search = s("//button[@class='SearchBox__button']")
    input_search = s("//input[@type = 'text']")
    input_search_active = s("//input[@type = 'text' and @class='SearchBox__input active']")
    input_search_active_string = "//input[@type = 'text' and @class='SearchBox__input active']"
    batton_favourites = s("(//div[@class='SvgIcon'])[2]")
    string_message_favourites_01 = s("//div[@class='headline-4']")
    button_close_favourites = s('//div[@class = "SvgIcon IButtonIcon"]')


    # locators burger menu

    hamburger_menu = s("(//div[@class='hamburger-menu burger'])[2]")
    hamburger_menu_string = "(//div[@class='hamburger-menu burger'])[2]"
    categoryes_link = ss("//li[@class='mainmenu__item']/a")
    category_parents_clothes = s("(//li[@class='mainmenu__item']/span)[1]")
    category_parents_lingerie = s("(//li[@class='mainmenu__item']/span)[2]")
    category_parents_accessories = s("(//li[@class='mainmenu__item']/span)[3]")
    category_parents_shoes = s("(//li[@class='mainmenu__item']/span)[4]")
    category_parents_special_offer = s("(//li[@class='mainmenu__item']/span)[5]")
    category_parents_campaigns = s("(//li[@class='mainmenu__item']/span)[6]")


    categoryes_sub = ss("//li[@class='mainmenu__item']/ul/li/a")
    categoryes_sub_sub = ss("//ul[@class='mainmenu-children mainmenu__children']/li/ul/li/a")


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
            self.browser_back()
            url_main_return = self.get_url()
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
        self.browser_back()
        url_main_return = self.get_url()
        self.wait_element(self.block_icon_string)  # ожидание блока иконок белого цвета
        self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")



    @allure.step('Переходы по разделам меню')
    def main_menu(self):
        self.click(self.batton_search, " поиск")
        self.wait_element(self.input_search_active_string)
        self.set_text(self.input_search_active, '6498-375', " инпут поиска")

        #доделать проверку после фикса бага

        self.click(self.batton_favourites, " избранное")
        message_fav = self.get_element_text(self.string_message_favourites_01, " строка экрана избранное").replace("\n", " ")
        self.assert_check_expressions("ВОЙДИТЕ ИЛИ ЗАРЕГИСТРИРУЙТЕСЬ, ЧТОБЫ ПРОСМОТРЕТЬ ВИШЛИСТ", message_fav, " ошибка сообщения на экране избранного")
        self.click(self.button_close_favourites, " закрыть избранное")

    @allure.step('Разделы меню каталога (ссылки)')
    def catalog_menu_link(self):
        self.click(self.hamburger_menu, " гамбургер меню")
        for i in range(len(self.categoryes_link)):
           #self.wait_element(self.hamburger_menu_string)
            self.click(self.categoryes_link[i], " раздел меню")
            time.sleep(1)
            url_catalog = self.get_url()
            self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
            self.browser_back()
            self.click(self.hamburger_menu, " гамбургер меню")

    @allure.step('Разделы меню ОДЕЖДА (выпадающие меню)')
    def catalog_menu_parents_link_clothes(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_clothes, " категория ОДЕЖДА")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории ОДЕЖДА ")
            time.sleep(1)
            url_catalog = self.get_url()
            if  url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_clothes, " категория ОДЕЖДА")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_clothes, " категория ОДЕЖДА")
                    self.click(self.categoryes_sub[i], " подраздел категории ОДЕЖДА ")

    @allure.step('Разделы меню НИЖНЕЕ БЕЛЬЕ (выпадающие меню)')
    def catalog_menu_parents_link_lingerie(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории НИЖНЕЕ БЕЛЬЕ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")
                    self.click(self.categoryes_sub[i], " подраздел категории НИЖНЕЕ БЕЛЬЕ ")

    @allure.step('Разделы меню АКСЕССУАРЫ (выпадающие меню)')
    def catalog_menu_parents_link_accessories(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории АКСЕССУАРЫ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")
                    self.click(self.categoryes_sub[i], " подраздел категории АКСЕССУАРЫ")

    @allure.step('Разделы меню ОБУВЬ (выпадающие меню)')
    def catalog_menu_parents_link_shoes(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_shoes, " категория ОБУВЬ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории ОБУВЬ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_shoes, " категория ОБУВЬ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_shoes, " категория ОБУВЬ")
                    self.click(self.categoryes_sub[i], " подраздел категории ОБУВЬ")

    @allure.step('Разделы меню СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ (выпадающие меню)')
    def catalog_menu_parents_link_special_offer(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
                    self.click(self.categoryes_sub[i], " подраздел категории СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")

    @allure.step('Разделы меню КОМПАНИИ (выпадающие меню)')
    def catalog_menu_parents_link_campaigns(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_campaigns, " категория КОМПАНИИ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории КОМПАНИИ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("summer", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_campaigns, " категория КОМПАНИИ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("summer", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_campaigns, " категория КОМПАНИИ")
                    self.click(self.categoryes_sub[i], " подраздел категории КОМПАНИИ")


























