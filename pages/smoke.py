import os
import time
import re

import allure
from selene.api import be, have, s
from selene.support.shared.jquery_style import ss

from pages.account import AccountPage
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.home import HomePage
from pages.login import LoginPage
from selene.api import browser

from pages.payment import PaymentPage
from selene.support.shared import browser
import random


class SmokePage(BasePage):

    # locators main page
    banners_main_image = ss("//div[@class = 'slide' and @style != 'cursor: pointer;']")
    video_main_image = ss("//video")
    block_icon_string = "//div[@class='App isHomepage page-index isAppNotify isEmptyCart']"
    block_icon_dark_theme = s("//div[@class='App isHomepage page-index isDark theme-isDark isEmptyCart']")
    block_icon_white_theme = s("//div[@class='App isHomepage page-index isAppNotify isEmptyCart']")

    first_catalog_image = s("(//picture/img)[1]")
    catalog_image = s("//picture/img")
    first_catalog_video = s("(//video[@class='d-none d-md-block'])[1]/source")
    catalog_video = s("//video/source")
    #first_catalog_video_attribute = s("(//video[@class='d-none d-md-block'])[1]//child::*")
    first_catalog_video_attribute = s("(//video[@class='d-none d-md-block'])[1]")
    #interesnaia_construkciya = s(//span[contains(@class,"mainmenu__link has-children")])
    all_bunners = ss("//div[@class='slide']")
    logo_string = "(//div[@class='logo'])[2]"

    # button main menu

    button_search = s("//button[@class='SearchBox__button']")
    input_search = s("//input[@type = 'text']")
    input_search_active = s("//input[@type = 'text' and @class='SearchBox__input active']")
    input_search_active_full =s("//input[@type = 'text' and @class='SearchBox__input fill active']")
    input_search_active_string = "//input[@type = 'text' and @class='SearchBox__input active']"
    product_in_result_search = s("//div[@class = 'CatalogProduct__title']")

    product_in_result_search_string = "//div[@class = 'CatalogProduct__title']"
    products_in_result_search = ss("//div[@class = 'CatalogProduct__title']/a")
    product_article = s("//div[@class='product__article']")
    message_search_not_result = s("//div[contains(text(), 'По вашему запросу ничего не найдено')]")

    button_favourites = s("(//div[@class='SvgIcon'])[2]")
    string_message_favourites_01 = s("//div[@class='headline-4']")
    button_close_favourites = s('//div[@class = "SvgIcon IButtonIcon"]')

    button_lk = s("(//div[@class='SvgIcon'])[1]")
    button_logout = s("//button[contains(text(), 'Выйти')]")
    button_login = s("//button[@class='btn btn-block btn-outline btn-primary']")
    button_login_string = "//button[@class='btn btn-block btn-outline btn-primary']"
    button_login_screen_login_string = "//button[@class='btn btn-block']"
    button_close_screen_login = s("//div[@class='SvgIcon IButtonIcon']")

    button_registration = s("//button[@class='btn btn-block btn-primary']")
    button_registration_string = "//button[@class='btn btn-block btn-primary']"
    button_registration_screen_registration_string = "//button[@class='btn btn-block']"
    button_registration_screen_registration = s("//button[@class='btn btn-block']")
    button_close_screen = s("//div[@class='SvgIcon IButtonIcon']")

    button_cart = s("(//div[@class='SvgIcon'])[4]")
    button_cart_2 =s("//a[@href='/cart' and @class='btn-control']")
    message_empty_cart = s("//div[@class='ViewCart__Empty__Message']/p")
    button_back_in_shop_empty_cart = s("//button[@class='btn ViewCart__Empty__Message__Button']")
    button_order_string = "//button[@class = 'btn btn-block']"



    # locators burger and catalog

    hamburger_menu = s("(//div[@class='hamburger-menu burger'])[2]")
    hamburger_menu_close = s("(//div[@class = 'hamburger-menu burger open']/div)[1]")
    hamburger_menu_string = "(//div[@class='hamburger-menu burger'])[2]"
    categoryes_link = ss("//li[@class='mainmenu__item']/a")
    category_parents_clothes = s("(//li[@class='mainmenu__item']/span)[1]")
    category_parents_lingerie = s("(//li[@class='mainmenu__item']/span)[2]")
    category_parents_accessories = s("(//li[@class='mainmenu__item']/span)[3]")
    category_parents_shoes = s("(//li[@class='mainmenu__item']/span)[3]")
    category_parents_special_offer = s("(//li[@class='mainmenu__item']/span)[4]")
    category_parents_campaigns = s("(//li[@class='mainmenu__item']/span)[5]")
    #categoryes_sub = ss("//li[@class='mainmenu__item']/ul/li/a")
    categoryes_sub = ss("//li[@class='mainmenu-children__item']/a")
    categoryes_sub_special_offer = ss("//span[@class='mainmenu__link has-children highlight delimiter']")
    categoryes_sub_sub = ss("//ul[@class='mainmenu-children mainmenu__children']/li/ul/li/a")

    block_catalog = s("//nav[@class='mainmenu']")
    cart = s("//span[@title = 'Ваша корзина пуста']")
    favourites = s("//a[@href='/cart' and @class='usermenu__link']")
    help = s("//a[@href='/help' and @class='usermenu__link']")
    #cart_bonus = s("//a[@href='/ru_ru#gift' and @class='usermenu__link']")
    cart_bonus = s("//a[@href='/ru_ru#gift']")
    card_bonus_text = s("//span[contains (text(), 'Электронные подарочные карты')]")
    account_or_name_user = s("//a[@href='/ru_ru#lk' and @class='usermenu__link']")
    dark_screen = s("//html[@style='overflow: hidden;']")
    element_plus = s("//div[@class='actions']")


    #locators login screen

    h1_srting = "//h1[contains(text(), 'Личный кабинет')]"
    link_help_string = "//a[@href = '/help' and contains(text(), 'Руководство по покупке')]"
    link_contacts_string = "//a[@href = '/contacts' and contains(text(), 'Контакты')]"
    link_about_string = "//a[@href = '/about' and contains(text(), 'Компания')]"
    link_shops_string = "//a[@href = '/shops' and contains(text(), 'Магазины')]"

    # locators registration screen

    message_registration_screen_string = "//div[contains(text(), 'Личные данные')]"
    button_change_password_string = "//button[contains(text(), 'Изменить пароль')]"
    button_save_changes_string = "//button[contains(text(), 'Сохранить изменения')]"
    message_mailing_string = "//span[contains(text(), 'Я хочу получать новостную рассылку')]"
    button_delete_accaunt_string ="//a[contains(text(), 'Удалить аккаунт')]"
    button_logout_account_string = "//button[contains(text(), 'Выйти')]"
    orders_string = "//div[@class = 'PreviewOrders__item']"
    message_orders_string = "//strong[contains(text(), 'Мои заказы')]"
    message_number_order = s("//div[@class = 'OrderComplete__note']/div")
    message_number_order_lk = s("//div[@class = 'PreviewOrders']/following-sibling::div")

    # favourities

    icon_favourities_empty = s("(//span[@class='badge'])[1]")
    #icon_favourities_01 =s("//a[contains(text(), 'Избранное')]/span[contains(text(), '1')]")
    #icon_favourities_01 = s("//a[contains(text(), 'Избранное')]")
    #icon_favourities_01 = s("//a[contains(text(), 'Лоферы из кожи шевро')]")
    icon_favourities_01 = s("(//span[@class='badge'])[1]")
    #icon_favourities_01 = s("//a[@href='/ru_ru/catalog/all_shoes#favorites']")
    icon_favourities_01_string = "//a[contains(text(), 'Избранное')]/span[contains(text(), '1')]"
    icon_fav_catalog = s("//button[@class='IButton CatalogProduct__bookmark isHover']")
    icon_fav_catalog_active = s("//button[@class='IButton CatalogProduct__bookmark isActive']")

    product_in_catalog = s("//button[@class='IButton CatalogProduct__bookmark']")
    products_in_catalog_random = ss("//img[@class='CatalogProduct__image lazyloaded']")

    img_in_catalog = s("//img[contains(@class,'CatalogProduct__image')]")
    img_in_cart_slider = s("//img[@class='MediaTape__object lazyloaded']")
    imges_in_cart_slider = ss("//img[contains(@class,'MediaTape__object ')]")
    title_product_in_cart = s("//h1[@class='product__title']")
    title_product_in_basket = s('//div[@class="CartTable__name"]/a/p')

    # Other

    list_url_cat = ["ru_ru/catalog/underwear_invisible", "ru_ru/catalog/palto_i_trench",
                    "ru_ru/catalog/underwear_microfiber", "ru_ru/catalog/bodysuits",
                    "ru_ru/catalog/loafers", "ru_ru/catalog/new", "ru_ru/catalog/sale_platya"]

    share_string_card_products = s("//a[contains(text(), 'Поделиться')]")

    # Basket

    counter_basket = s("(//span[@class='badge'])[2]")

    address_courier = s("//a[contains(text(), 'Добавить новый адрес')]")
    field_address_surname = s("//input[@placeholder='Фамилия']")
    field_address_name = s("//input[@placeholder='Имя']")
    field_address_number = s("//input[@class='vti__input']")
    field_address_e_mail = s("//input[@placeholder='E-mail']")
    field_address_town = s("//textarea[@placeholder='Город / населенный пункт']")
    autocomplit_town = s("//li[@id='autocomplete-result-0']")
    field_address_street = s("//textarea[@placeholder='Улица и дом']")
    field_address_door = s("//input[@placeholder='Квартира']")
    button_address_save = s("//button[@class='btn btn-block']")


    card_bonus = s("//span[contains(text(),'Подарочной картой')]")
    field_card_bonus_number = s("//input[@placeholder='Номер карты']")

    field_card_bonus_sum = s("//input[@placeholder='Сумма к списанию']")
    field_card_bonus_pin = s("//input[@placeholder='Пин-код']")
    price_without_discount_text = s('(//div[@class="CustomerCartSummary__value"])[4]/span')

























    # ОСНОВНОЙ ЭКРАН

    @allure.step('Цикл проверки баннеров')
    def cycle_banners(self):

        for i in range(len(self.banners_main_image)):
            list_first_attribute_banners = ['https://cache-limeshop.cdnvideo.ru/limeshop/aa/740493936811267570dfa11ee9db500155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/7381001681ca62c1ceb2511ed9da900155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/7310296803a1cc11e539611ed9d6e00155d011401.jpeg?q=85&w=440']
            url_main = self.get_url()

            self.move_to(browser.driver.find_element_by_xpath("(//div[@class = 'slide' and @style != 'cursor: pointer;'])["+(str(i+1))+"]"))
            self.click(self.banners_main_image[i], " баннер")
            first_image = self.get_attribute(self.first_catalog_image, "data-src")
            self.assert_check_expressions(list_first_attribute_banners[i], first_image, " некорректное отображение порядка товаров в каталоге")
            self.browser_back()
            url_main_return = self.get_url()
            # добавить когда испраявят баг на накст 01
            #self.wait_element_assure(self.block_icon_white_theme)  # ожидание блока иконок белого цвета
            #self.wait_element_assure(self.block_icon_dark_theme) #ожидание блока иконок черного цвета
            self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")

    @allure.step('Проверка видео')
    def video(self):
        for i in range(len(self.video_main_image)):
            list_first_attribute_banners = ['https://cache-limeshop.cdnvideo.ru/limeshop/2023/07/13/43de35d624baff5fce94dd268af8a9d3ed62bc3f.mp4']
            url_main = self.get_url()

            self.move_to(browser.driver.find_element_by_xpath("(//video)[" + (str(i + 1)) + "]"))
            self.click(self.video_main_image[i], " видео")
            first_image = self.get_attribute(self.catalog_video, "src")
            self.assert_check_expressions(list_first_attribute_banners[i], first_image,
                                          " некорректное отображение порядка товаров в каталоге")
            first_video_loop = self.get_attribute(self.first_catalog_video_attribute, "loop")
            self.assert_check_expressions("true", first_video_loop,
                                          " нет тега автовоспроизведения видео")
            self.browser_back()
            url_main_return = self.get_url()
            self.wait_element_assure(self.block_icon_dark_theme)  # ожидание блока иконок черного цвета
            self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")
            break



        # video = 'https://cache-limeshop.cdnvideo.ru/limeshop/landing-pages/summer-basic-23/01_desc+ipad.mp4'
        # url_main = self.get_url()
        # self.click(self.video_main_image, " видео")
        # first_video = self.get_attribute(self.first_catalog_video_attribute, "src")
        # self.assert_check_expressions(video, first_video,
        #                               " некорректное отображение видео в каталоге")
        # first_video_loop = self.get_attribute(self.first_catalog_video, "loop")
        # self.assert_check_expressions("true", first_video_loop,
        #                               " нет тега автовоспроизведения видео")
        # self.browser_back()
        # url_main_return = self.get_url()
        # self.wait_element(self.block_icon_string)  # ожидание блока иконок белого цвета
        # self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")

    @allure.step('Проверка логотипа')
    def logo(self):
        for i in range(len(self.all_bunners)):
            self.move_to(browser.driver.find_element_by_xpath("(//div[@class='slide'])["+(str(i+1))+"]"))
            #self.move_to(self.all_bunners[i])
            self.wait_element(self.logo_string)

    @allure.step('Поиск в главном меню')
    def main_menu_search(self):
        self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active)
        self.set_text(self.input_search_active, '6498-375', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        self.wait_element_assure(self.product_in_result_search)

        for i in range(len(self.products_in_result_search)):
            self.click(self.products_in_result_search[i], " продукт в результатах поиска")
            self.wait_element_assure(self.product_in_result_search)
            article_text = self.get_element_text(self.product_article, " артикул товара")
            article = article_text.partition(" ")[2]
            self.assert_check_expressions(article, "6498-375", " значение артикула не соответствует")
            self.browser_back()
            self.wait_element_assure(self.product_in_result_search)

        self.field_clear(self.input_search_active_full, " инпут поиска")
        self.set_text(self.input_search_active_full, 'платье', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        time.sleep(3)
        self.wait_element_assure(self.product_in_result_search)
        for y in range(len(self.products_in_result_search)):
            product_text = self.get_element_text(self.products_in_result_search[y], " название товара куртка").lower()
            print(product_text)
            self.assert_check_coincidence("платье", product_text, " некорреткный вывод результатов поиска")

    @allure.step('Разделы меню каталога (ссылки)')
    def catalog_menu_link(self):
        self.click(self.hamburger_menu, " гамбургер меню")
        for i in range(len(self.categoryes_link)):
           #self.wait_element(self.hamburger_menu_string)
            self.click(self.categoryes_link[i], " раздел меню")
            time.sleep(2)
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
            time.sleep(2)
            url_catalog = self.get_url()
            if  url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                time.sleep(1)
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_clothes, " категория ОДЕЖДА")
                time.sleep(1)


            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(2)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в подкаталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    time.sleep(1)
                    self.click(self.category_parents_clothes, " категория ОДЕЖДА")
                    self.click(self.categoryes_sub[i], " подраздел категории ОДЕЖДА ")
                    time.sleep(1)

    @allure.step('Разделы меню НИЖНЕЕ БЕЛЬЕ (выпадающие меню)')
    def catalog_menu_parents_link_lingerie(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории НИЖНЕЕ БЕЛЬЕ")
            time.sleep(2)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                time.sleep(1)
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")
                time.sleep(1)

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(2)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    time.sleep(1)
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")
                    self.click(self.categoryes_sub[i], " подраздел категории НИЖНЕЕ БЕЛЬЕ ")
                    time.sleep(1)

    @allure.step('Разделы меню АКСЕССУАРЫ (выпадающие меню)')
    def catalog_menu_parents_link_accessories(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории АКСЕССУАРЫ")
            time.sleep(2)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("summer", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                time.sleep(1)
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")
                time.sleep(1)

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(2)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    time.sleep(1)
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")
                    self.click(self.categoryes_sub[i], " подраздел категории АКСЕССУАРЫ")
                    time.sleep(1)

    @allure.step('Разделы меню ОБУВЬ (выпадающие меню)')
    def catalog_menu_parents_link_shoes(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_shoes, " категория ОБУВЬ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории ОБУВЬ")
            time.sleep(2)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                time.sleep(1)
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_shoes, " категория ОБУВЬ")
                time.sleep(1)

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(2)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    time.sleep(1)
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_shoes, " категория ОБУВЬ")
                    self.click(self.categoryes_sub[i], " подраздел категории ОБУВЬ")
                    time.sleep(1)

    @allure.step('Разделы меню СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ (выпадающие меню)')
    def catalog_menu_parents_link_special_offer(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
            time.sleep(3)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                time.sleep(1)
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
                time.sleep(1)

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(2)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    time.sleep(1)
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
                    self.click(self.categoryes_sub[i], " подраздел категории СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
                    time.sleep(1)

    @allure.step('Разделы меню КОМПАНИИ (выпадающие меню)')
    def catalog_menu_parents_link_campaigns(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_campaigns, " категория КОМПАНИИ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории КОМПАНИИ")
            time.sleep(2)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("summer", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                time.sleep(1)
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_campaigns, " категория КОМПАНИИ")
                time.sleep(1)

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(2)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("summer", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    time.sleep(1)
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_campaigns, " категория КОМПАНИИ")
                    self.click(self.categoryes_sub[i], " подраздел категории КОМПАНИИ")
                    time.sleep(1)

    # ПРОФИЛЬ

    @allure.step('Профиль / экран вход/регистрация')
    def login_screen(self):

        self.wait_element(self.h1_srting)
        self.wait_element(self.link_help_string)
        self.wait_element(self.link_contacts_string)
        self.wait_element(self.link_about_string)
        self.wait_element(self.link_shops_string)
        self.wait_element(self.button_login_string)
        self.wait_element(self.button_registration_string)
        self.click(self.button_close_screen, " закрыть экран входа\регистрации")

    @allure.step('Логин с невалидным паролем')
    def user_login_not_valid(self):

        #page = HomePage()
        self.click(self.button_lk, " личный кабинет")

        page = AccountPage()
        page.click_enter_btn()
        time.sleep(3)

        page = LoginPage()
        page.login(email="chernikov.kv3@lime-shop.com", password=("VTer38XXXXXX"))
        page.check_login_error()

    @allure.step('Успешный логин')
    def user_login(self):

        self.click(self.button_lk, " кнопка Личный кабинет")
        page = AccountPage()
        page.click_enter_btn()
        page = LoginPage()
        page.login(email=os.getenv("test_user"), password=os.getenv("password"))
        page.check_logout_btn_is_visible()

    @allure.step('Разлогин')
    def user_logout(self):

        self.click(self.button_lk, " кнопка Личный кабинет")
        self.wait_element_assure(self.button_logout)
        self.click(self.button_logout, " кнопка выход из ЛК")

    @allure.step('Успешный логин второй пользователь')
    def user2_login(self):

        self.click(self.button_lk, " кнопка Личный кабинет")
        page = AccountPage()
        page.click_enter_btn()
        page = LoginPage()
        page.login(email=os.getenv("test_user2"), password=os.getenv("password"))
        page.check_logout_btn_is_visible()

    @allure.step('Регистрация с не валидными данными')
    def user_registration_not_valid(self):
        # page = HomePage()
        self.click(self.button_lk, " личный кабинет")
        page = HomePage()
        page.click_registration_btn()
        page.fill_registration_fields_smoke()

        list_errors = page.get_text_error_smoke()

        assert list_errors[0] == ('некорректный e-mail'), print('Некорректный текст ошибки регистрации')
        assert list_errors[1] == ('некорректный номер телефона'), print('Некорректный текст ошибки регистрации')
        assert list_errors[2] == ('введенные пароли не совпадают'), print('Некорректный текст ошибки регистрации')

    @allure.step('Регистрация с валидными данными ')
    def user_registration(self):
        page = HomePage()

        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields()
        page = LoginPage()
        page.wait_element_assure(page.logout_btn)

    @allure.step('Первый вход в профиль')
    def user_first_lk(self):
        page = HomePage()

        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields()
        page = LoginPage()
        page.check_logout_btn_is_visible()

        self.wait_element(self.message_registration_screen_string)
        self.wait_element(self.button_change_password_string)
        self.wait_element(self.button_save_changes_string)
        #self.wait_element(self.message_mailing_string)
        self.wait_element(self.button_delete_accaunt_string)
        self.wait_element(self.button_logout_account_string)

    @allure.step('Мои данные (профиль с покупками)')
    def user_profile_with_order(self):

        page = PaymentPage()
        page.preview_payment()
        page.check_product_for_order()
        page.to_pay_btn.click()
        time.sleep(2)
        page.success_btn.click()


        #number_order = self.get_element_text(self.message_number_order, " стрка с номером заказа")
        number_order = (re.sub('[^0-9]', "", self.get_element_text(self.message_number_order, ' сумма заказа после оформления')))


        self.click(self.button_lk, " личный кабинет")

        self.wait_element(self.message_registration_screen_string)
        self.wait_element(self.button_change_password_string)
        self.wait_element(self.button_save_changes_string)
        self.wait_element(self.message_mailing_string)
        self.wait_element(self.button_delete_accaunt_string)
        self.wait_element(self.button_logout_account_string)
        self.wait_element(self.message_orders_string)
        time.sleep(10)
        self.wait_element(self.orders_string)


        number_ord = (re.sub('[^0-9]', "", self.get_element_text(self.message_number_order_lk, ' сумма заказа в личном кабинете')))
        number_order_lk = number_ord[:-12]

        self.assert_check_expressions(number_order, number_order_lk, " оформленный заказ отсутсвует в личном кабинете")

    @allure.step('Поиск по тексту')
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/881")
    def search_successful_text(self):
        self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active)
        self.set_text(self.input_search_active, 'очки', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        time.sleep(3)
        self.wait_element_assure(self.product_in_result_search)
        for i in range(len(self.products_in_result_search)):
            product_text = self.get_element_text(self.products_in_result_search[i], " название товара Очки").lower()
            print(product_text)
            self.assert_check_coincidence("очки", product_text, " некорреткный вывод результатов поиска")

    @allure.step('Поиск по артикулу')
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/882")
    def search_successful_article(self):
        #self.click(self.button_search, " поиск")
        self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active)
        self.set_text(self.input_search_active, '1418-888', " инпут поиска")
        time.sleep(3)
        self.push_enter(self.input_search_active_full, " инпут поиска")
        self.wait_element_assure(self.product_in_result_search)

        for i in range(len(self.products_in_result_search)):

            self.click(self.products_in_result_search[i], " продукт в результатах поиска")
            self.wait_element_assure(self.product_in_result_search)
            article_text = self.get_element_text(self.product_article, " артикул товара")
            article = article_text.partition(" ")[2]
            self.assert_check_expressions(article, "1418-888", " значение артикула не соответствует")
            self.browser_back()

            self.wait_element_assure(self.product_in_result_search)

    @allure.step('Поиск без результата')
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/883")
    def search_not_result(self):
        #self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active_full)
        self.set_text(self.input_search_active_full, 'фуфайка', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        self.wait_element_assure(self.message_search_not_result)



    @allure.step('Добавление в избранное из каталога')
    def add_favourites_catalog(self):

        page = CatalogPage()
        time.sleep(5)
        self.wait_element_assure(self.product_in_result_search)
        page.move_to(browser.driver.find_element_by_xpath("//a[@class='CatalogProduct__image-link']//img"))
        self.click(self.icon_fav_catalog, " элемент избранного в каталоге")

    @allure.step('Удаление из избранного через  каталог')
    def del_favourites_catalog(self):

        page = CatalogPage()
        time.sleep(3)
        self.wait_element_assure(self.product_in_result_search)
        page.move_to(browser.driver.find_element_by_xpath("//a[@class='CatalogProduct__image-link']//img"))
        time.sleep(1)
        self.click(self.icon_fav_catalog_active, " элемент избранного в каталоге")

    @allure.step('Добавление в избранное из карточки')
    def add_favourites_cart(self):

        page = CatalogPage()
        time.sleep(3)
        self.wait_element_assure(self.product_in_result_search)
        #page.move_to(browser.driver.find_element_by_xpath("//div[@class='CatalogProduct__price']"))
        self.click(self.img_in_catalog, " карточка товара")
        page.wait_element_assure(page.add_favorite_btn)
        page.click(page.add_favorite_btn, " добавить товар в избранное")




    @allure.step('Проверка элемента избранное в меню')
    def check_element_fav_menu(self):
        time.sleep(1)
        self.wait_element_assure(self.icon_favourities_01)
        value_fav = self.get_element_text(self.icon_favourities_01, " получить значение элемента избранное")
        return value_fav

    @allure.step('Проверка пустого элемента избранное в меню')
    def check_element_fav_empty_menu(self):
        time.sleep(1)
        #self.wait_element_assure(self.icon_favourities_empty)
        value_fav = self.get_element_text(self.icon_favourities_empty, " получить значение элемента избранное")
        return value_fav

    @allure.step('Удаление из избранного в карточке')
    def del_favourites_cart_product(self):
        page = CatalogPage()
        page.click(page.favorites_btn, " избранное")
        page.click(page.product_in_favourites_screen, " карточку товара")
        page.wait_element_assure(page.add_favorite_btn)
        page.click(page.add_favorite_btn, " удалить товар из избранного")


    @allure.step('Проверка отсутсвия товара после удаления на экране Избранное (из карточки товара)')
    def check_del_product_fav_screen(self):

        title_del_fav = self.get_element_text(self.title_product_in_cart, " название товара в карточке")
        page = CatalogPage()
        page.click(page.favorites_btn, " избранное")
        time.sleep(3)
        page.click(page.product_in_favourites_screen, " карточку товара" )
        time.sleep(1)
        title_not_del_fav = self.get_element_text(self.title_product_in_cart, " название товара в карточке")
        self.assert_check_not_expressions(title_del_fav, title_not_del_fav, " товар не удален из избранного")

    @allure.step('Проверка наличия товара на экране Избранное (из карточки товара)')
    def check_add_fav(self):

        title_fav = self.get_element_text(self.title_product_in_cart, " название товара в карточке")
        page = CatalogPage()
        page.click(page.favorites_btn, " избранное")
        page.click(page.product_in_favourites_screen, " карточку товара")
        title_fav_screen = self.get_element_text(self.title_product_in_cart, " название товара в карточке")
        self.assert_check_expressions(title_fav, title_fav_screen, " товар отсутсвует в избранном")

    @allure.step('Проверка пустого экрана избранного')
    def check_full_screen_fav(self):
        page = CatalogPage()
        page.click(page.favorites_btn, " избранное")
        page.wait_element_not_visible(page.product_in_favourites_screen_string)

    @allure.step("Рандомный подраздела каталога")
    def click_random_cat(self):
        random.choice(self.categoryes_sub).click()

    @allure.step("Рандомный url каталога")
    def click_random_cat_url(self):

        random_cat = random.choice(self.list_url_cat)
        return random_cat

    @allure.step("Рандомный товар каталога")
    def click_random_product(self):
        random.choice(self.products_in_catalog_random).click()

    @allure.step('Проверка счетчика корзины')
    def check_counter_basket(self):
        time.sleep(1)
        self.wait_element_assure(self.counter_basket)
        value_counter_basket = self.get_element_text(self.counter_basket, " получить значение счетчика корзины")
        return value_counter_basket

    @allure.step('Добавление другого адреса доставки курьером')
    def add_address_courier(self):
        self.click(self.address_courier, " добавить адрес курьерской доставки")
        self.wait_element_assure(self.field_address_surname)
        self.set_text(self.field_address_surname, "Surname", " заполнение поля фамилия")
        self.set_text(self.field_address_name, "Name", " заполнение поля Имя")
        self.set_text(self.field_address_number, "9998887766", " заполнение поля номера телефона")
        self.set_text(self.field_address_e_mail, "Email@mail.ru", " заполнение поля почты")
        self.set_text(self.field_address_town, "Новосибирск", " заполнение поля города")
        self.click(self.autocomplit_town, " выбор города в атокомплите")
        self.set_text(self.field_address_street, "Иванова 1", " заполнение поля адреса")
        self.click(self.autocomplit_town, " выбор улицы в атокомплите")
        self.set_text(self.field_address_door, "1", " заполнение поля квартира")
        self.click(self.button_address_save, " сохранить новый адресс")

    @allure.step('Оплата подарочной картой 50000')
    def payment_bonus_card(self):
        self.click(self.card_bonus, " подарочная карта")
        self.set_text(self.field_card_bonus_number, "7012495883190627", " заполнение поля номера подарочной карты")

        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text,
                                                                                 'Получение суммы заказа без промо'))))


        self.set_text(self.field_card_bonus_sum, price_without_discount, " заполнение поля номера подарочной карты")
        self.set_text(self.field_card_bonus_pin, "3550", " заполнение поля пинкода")

    @allure.step('Оплата подарочной картой с промо')
    def payment_bonus_card_promocode(self):
        self.click(self.card_bonus, " подарочная карта")
        self.set_text(self.field_card_bonus_number, "7012495883190627", " заполнение поля номера подарочной карты")

        self.set_text(self.field_card_bonus_sum, 100, " заполнение поля номера подарочной карты")
        time.sleep(3)
        self.set_text(self.field_card_bonus_pin, "3550", " заполнение поля пинкода")
        time.sleep(3)

    @allure.step('Оплата подарочной картой недостаточно средств')
    def payment_bonus_card_no_many(self):
        self.click(self.card_bonus, " подарочная карта")
        self.set_text(self.field_card_bonus_number, "6088490568745006", " заполнение поля номера подарочной карты")
        time.sleep(3)
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промо'))))

        self.set_text(self.field_card_bonus_sum, price_without_discount, " заполнение поля номера подарочной карты")
        self.set_text(self.field_card_bonus_pin, "6474", " заполнение поля пинкода")



    @allure.step('Оплата подарочной картой не валидная ')
    def payment_bonus_card_not_valid(self):
        self.click(self.card_bonus, " подарочная карта")
        self.set_text(self.field_card_bonus_number, "6088490568745111", " заполнение поля номера подарочной карты")

        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text,
                                                                                 'Получение суммы заказа без промо'))))

        self.set_text(self.field_card_bonus_sum, price_without_discount, " заполнение поля номера подарочной карты")


    # @allure.step('Добавление в избранное из карточки несколько товаров')
    # def add_favourites_cart_product(self):
    #
    # @allure.step('Удаление из избранного через каталог')
    # def del_favourites_catalog(self):
    #
    # @allure.step('Удаление из избранного в карточке')
    # def del_favourites_cart_product(self):








































































