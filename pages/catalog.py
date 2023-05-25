import os
import random
import time
import re

import allure
from selene.api import *

from pages.base import BasePage
from selene.support.shared import browser


class CatalogPage(BasePage):
    # Locators
    #hamburger_menu = s("//div[@class='icon']")
    hamburger_menu = s("(//div[@class='hamburger-menu burger'])[2]")

    hamburger_menu_string = "//div[@class='icon']"
    menu_link_clothes = s("//span[span= 'Одежда']")
    menu_chapter = s("//a[span ='БРЮКИ']")
    menu_subsection = s("//a[@class = 'mainmenu-children__link' and span ='ЛЕГИНСЫ']")
    choose_a_product = s("//a[@class='CatalogProduct__image-link']//img")
    choose_a_product_str = "//a[@class='CatalogProduct__image-link']//img"

    add_to_cart = s("//button[@class ='btn btn-cart']")
    basket_btn = s("//a[@href ='/cart' and @class='btn-control']")
    colors_selector = ss("//div[@class='ColorSelector__imageBox']")
    drop_down_size = s("//div[@class='SizeSelector__header']")
    button_drop_down_size = s("//div[@class='SizeSelector__arrow']")
    sizes_list = ss("//span[@class='SizeSelector__title']")
    title_text = s("//h1[@class='product__title']")
    product_price_text = s("//div[@class='product__price']")
    product_article_text = s("//div[@class='product__article']")
    product_color_text = s("//div[@class='ColorSelector product__colors']")
    product_size_text = s("//div[@class='SizeSelector__selected']")
    add_favorite_btn = s("//div[@class='actions__fav']")
    favorites_btn = s("//a[contains(@href,'#favorites') and @class='btn-control']")
    choose_a_product_in_favorite = s("//img[@class='PreviewGoods__img']")
    first_card = s("(//a[@class='CatalogProduct__image-link'])[1]")
    last_card = s("//a[@class= 'PreviewGoods__imageBox']/a")
    menu_blazers = s("//a[@class = 'mainmenu-children__link' and span ='БЛЕЙЗЕРЫ']")
    product_in_catalog = s("(//button[@class='IButton CatalogProduct__bookmark'])[1]")
    menu_link_bags = s("//a[span= 'СУМКИ']")
    menu_link_new = s("//a[span= 'НОВИНКИ']")
    choose_a_product_bags = s("//div[@class= 'CatalogProduct__title']/a")
    menu_link_shoes = s("//span[span= 'ОБУВЬ']")
    menu_subsection_shoes = s("//a[@class= 'mainmenu-children__link' and span = 'Ботильоны']")
    menu_subsection_shoes_01_all_models = s("//a[@class= 'mainmenu-children__link' and span = 'ВСЕ МОДЕЛИ']")
    menu_subsection_shoes_lofers = s("//a[@class= 'mainmenu-children__link' and span = 'ЛОФЕРЫ']")
    menu_subsection_shoes_botil = s("//a[@class= 'mainmenu-children__link' and span = 'Ботильоны']")

    menu_section_shoes = s("//span[@class= 'mainmenu__link has-children delimiter' and span = 'ОБУВЬ']")

    choose_a_product_shoes = s("(//a[@href = '/product/12598_9626_094-bezevyi'])[2]")
    menu_link_lingerie = s("//span[span= 'НИЖНЕЕ БЕЛЬЕ']")
    menu_subsection_all_models = s("//a[@class= 'mainmenu-children__link' and span = 'ВСЕ МОДЕЛИ']")
    menu_subsection_body = s("//a[@class= 'mainmenu-children__link' and span = 'БОДИ']")
    menu_subsection_linearge_briefs = s("//a[@class= 'mainmenu-children__link' and span = 'БОДИ']")
    choose_a_product_lingerie = s("(//a[@href= '/product/12463_8035_966-svetlyi_xaki'])[1]")
    first_product_in_catalog = s(
        "//button[contains(@class, 'isActive')]/ancestor::div[contains(@class, 'CatalogRow ')]//a")
    choose_a_product_svetlyi_xaki = s("(//a[@href='/product/12718_9717_920-svetlyi_xaki'])[1]")
    menu_chapter_accessories = s("//span[span= 'АКСЕССУАРЫ']")
    menu_subsection_belts = s("//a[@class= 'mainmenu-children__link' and span = 'РЕМНИ']")
    choose_a_product_belts = s("(//a[@href= '/product/12843_9898_293-cernyi'])[2]")
    #choose_a_product_1399 = s('//a[contains(text(), "Бюстгальтер с треугольными чашками и узлом")]')
    choose_a_product_1399 = s('(//a[contains(text(), "Боди без рукавов")])[3]')
    choose_a_product_loafers = s('//a[contains (text(), "Лоферы из кожи шевро")]')
    menu_subsection_shoes_all = s("//a[@class= 'mainmenu-children__link' and span = 'ВСЕ МОДЕЛИ']")

    icon_favourities_full = s("//a[@disabled='disabled']")
    product_in_favourites_screen = s("//img[@class = 'PreviewGoods__img']")
    product_in_favourites_screen_string = "//img[@class = 'PreviewGoods__img']"
    products_in_favourites_screen = ss("//img[@class = 'PreviewGoods__img']")
    button_close_fav = s("//div[@class='SvgIcon IButtonIcon']")

    menu_link_special = s("//span[span= 'СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ']")
    menu_subsection_all_models_special = s("//a[@class= 'mainmenu-children__link highlight' and span = 'ВСЕ МОДЕЛИ']")

    img_in_catalog = s("//img[contains(@class,'CatalogProduct__image')]")





    @allure.step("Добавление в корзину")
    def add_to_basket(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_clothes, "Блок ОДЕЖДА")
        self.click(self.menu_chapter, " раздел Брюки")
        self.click(self.menu_subsection, " подраздел Легинсы")
        self.click(self.choose_a_product, "Выброр товара")
        time.sleep(1)
        self.click_random_color()
        time.sleep(1)
        self.click_random_size()
        time.sleep(1)


        title = self.get_element_text(self.title_text, 'Заголовок')
        price = self.get_element_text(self.product_price_text, 'Цена')
        article = self.get_element_text(self.product_article_text, 'Артикул')
        color = self.get_element_text(self.product_color_text, 'Цвет')
        size = self.get_element_text(self.product_size_text, 'Размер')

        return title, price, article, color, size

    @allure.step("Рандомный выбор цвета")
    def click_random_color(self):
        random.choice(self.colors_selector).click()

    @allure.step("Рандомный выбор размера")
    def click_random_size(self):
        self.drop_down_size.click()
        time.sleep(2)
        random.choice(self.sizes_list).click()





    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_clothes, " Блок ОДЕЖДА")
        self.click(self.menu_chapter, " Раздел Брюки")
        self.click(self.menu_subsection, " подраздел Легинсы")
        url_first_card = self.get_attribute(self.first_card, "href").partition('product/')[2]
        self.click(self.choose_a_product, "Выбор товара")
        time.sleep(2)
        assert url_first_card in self.get_url()
        self.click(self.add_favorite_btn, "Добавка в избранное")
        self.click(self.favorites_btn, "переход в избранное")
        time.sleep(2)
        url_last_card = self.get_attribute(self.last_card, "href").partition('product/')[2]
        self.click(self.choose_a_product_in_favorite, "выбор товара в избранном")
        assert url_last_card in self.get_url()
        self.click(self.add_favorite_btn, "Удаление из избранного")
        self.click(self.favorites_btn, "переход в избранное")
        time.sleep(2)

        assert url_first_card == url_last_card, print('Урл отличается')




    @allure.step("Добавление в избранное из каталога")
    def add_to_favorites_in_catalog(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_clothes, " Блок ОДЕЖДА")
        self.click(self.menu_blazers, " Ссылка БЛЕЙЗЕРЫ")
        time.sleep(1)
        self.move_to(browser.driver.find_element_by_xpath("//a[@class='CatalogProduct__image-link']//img"))
        time.sleep(1)
        self.click(self.product_in_catalog, "избранное в каталоге")
        url_first_card = self.get_attribute(self.first_product_in_catalog, "href").partition('product/')[2]
        self.click(self.favorites_btn, "переход в избранное")
        time.sleep(1)
        url_last_card = self.get_attribute(self.last_card, "href").partition('product/')[2]

        assert url_first_card == url_last_card, print('Урл отличается')




    @allure.step("Добавление в корзину несколько товаров")
    def basket_multiple_products(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_bags, " Ссылка СУМКИ")
        self.wait_element_assure(self.choose_a_product)
        self.click(self.choose_a_product, "товар сумка")
        price_bags = self.get_element_text(self.product_price_text, 'цена сумки')
        self.click(self.add_to_cart, "добавить в корзину")
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_shoes, "Блок ТУФЛИ")
        self.click(self.menu_subsection_shoes, "Ссылка БОТИЛЬОНЫ")
        self.click(self.choose_a_product, "Товар ботильоны")
        self.click(self.add_to_cart, "добавить в корзину")
        price_shoes = self.get_element_text(self.product_price_text, 'цена туфли')


        return price_shoes, price_bags

    @allure.step("Добавление товара в корзину")
    def basket_changes_products(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_chapter_accessories, "Блок АКССЕСУАРЫ")
        self.click(self.menu_subsection_belts, "Раздел РЕМНИ")
        self.click(self.choose_a_product, "Товар РЕМНИ")
        self.click(self.add_to_cart, "добавить в корзину")
        time.sleep(1)
        price_belts = re.sub('[^0-9]', "",
                                 self.get_element_text(self.product_price_text, 'Цена товара'))

        return price_belts

    @allure.step("Добавление товара в корзину 1999 рублей")
    def basket_changes_products_1399(self):
        time.sleep(5)
        self.open_url(os.getenv('base_url') + "/ru_ru/catalog/bodysuits")

        self.click(self.choose_a_product_1399, "Товар с ценой 1999")
        time.sleep(2)
        self.click(self.add_to_cart, "добавить в корзину")
        time.sleep(1)

    @allure.step("Добавление в корзину единственного товара")
    def basket_add_last_product(self):
        # Подобрать товар
        time.sleep(5)

        self.open_url(os.getenv('base_url') + "/ru_ru/catalog/underwear_invisible")
        self.click(self.choose_a_product_1399, "Товар с ценой 1999")
        time.sleep(2)
        self.click(self.add_to_cart, "добавить в корзину")
        time.sleep(1)

    @allure.step("Добавление в корзину товара со скидкой")
    def basket_add_discount_product(self):
        time.sleep(5)
        # self.wait_element(self.hamburger_menu_string)
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_special, "Блок Специальное предложение")
        self.click(self.menu_subsection_all_models_special, "Подраздел Все модели")
        self.click(self.img_in_catalog, "Товар со скидкой")
        time.sleep(2)
        self.click(self.add_to_cart, "добавить в корзину")
        time.sleep(1)

    @allure.step("Добавление нескольких товаров в корзину")
    def basket_add_many_products(self):

        self.open_url(os.getenv('base_url') + "/ru_ru/catalog/bodysuits")
        self.click(self.choose_a_product_1399, "Товар с ценой 1999")
        self.click(self.add_to_cart, "добавить в корзину")
        time.sleep(1)
        #self.open_url(os.getenv('base_url') + "/ru_ru/catalog/loafers")
        self.open_url(os.getenv('base_url') + "/ru_ru/catalog/loafers")
        self.click(self.choose_a_product_loafers, "Товар лоферы")
        self.click(self.add_to_cart, "добавить в корзину")
        time.sleep(1)

    @allure.step("Переход в каталог Обувь Все модели")
    def select_section_menu_shoes_all(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_shoes, "Секция Обувь")
        self.click(self.menu_subsection_shoes_01_all_models, "Раздел Все модели")

    @allure.step("Переход в каталог Нижнее белье  Все модели")
    def select_section_menu_lingerie_all(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_lingerie, "Блок Нижнее белье")
        self.click(self.menu_subsection_body, "Подраздел Все модели")

    @allure.step("Переход в каталог Сумки")
    def select_section_menu_bags(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_bags, "Блок Сумки")

    @allure.step("Переход в каталог Новинки")
    def select_section_menu_new(self):
        self.click(self.hamburger_menu, "гамбургер-меню")
        self.click(self.menu_link_new, "Блок Новинки")


    @allure.title("Очистка избранного")
    def favoutites_clear(self):

       #self.wait_element_assure(self.block_product)
        self.click(self.favorites_btn, " избранное")
        time.sleep(4)

        try:
            for i in range(len(self.products_in_favourites_screen)):
                time.sleep(2)
                self.click(self.product_in_favourites_screen, " превью товара на экране избранного")
                time.sleep(1)
                self.wait_element_assure(self.add_favorite_btn)
                self.click(self.add_favorite_btn, " удалить товар из избранного")
                time.sleep(3)
                self.click(self.favorites_btn, " избранное")

            self.click(self.product_in_favourites_screen, " превью товара на экране избранного")
            time.sleep(1)
            self.wait_element_assure(self.add_favorite_btn)
            self.click(self.add_favorite_btn, " удалить товар из избранного")
            time.sleep(3)
            self.click(self.favorites_btn, " избранное")
            self.click(self.button_close_fav, " закрыть экран избранного")
            time.sleep(2)

        except:
            pass











