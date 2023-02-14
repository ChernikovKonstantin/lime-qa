import random
import time

import allure
from selene.api import *

from pages.base import BasePage


class CatalogPage(BasePage):
    # Locators
    hamburger_menu = s("//div[@class='icon']")
    menu_link_clothes = s("//span[span= 'Одежда']")
    menu_chapter = s("//a[span ='БРЮКИ']")
    menu_subsection = s("//a[@class = 'mainmenu-children__link' and span ='ЛЕГИНСЫ']")
    choose_a_product = s("//a[@class='CatalogProduct__image-link']//img")
    add_to_cart = s("//button[@class ='btn btn-cart']")
    basket_btn = s("//a[@href ='/cart' and @class='btn-control']")
    colors_selector = ss("//div[@class='ColorSelector__imageBox']")
    drop_down_size = s("//div[@class='SizeSelector__header']")
    sizes_list = ss("//span[@class='SizeSelector__title']")
    title_text = s("//h1[@class='product__title']")
    product_price_text = s("//div[@class='product__price']")
    product_article_text = s("//div[@class='product__article']")
    product_color_text = s("//div[@class='ColorSelector product__colors']")
    product_size_text = s("//div[@class='SizeSelector__selected']")
    add_favorite_btn = s("//div[@class='actions__fav']")
    favorites_btn = s("//a[contains(@href,'#favorites') and @class='btn-control']")
    choose_a_product_in_favorite = s("//img[@class='PreviewGoods__img']")

    @allure.step("Добавление в корзину")
    def add_to_basket(self):
        self.hamburger_menu.click()
        self.menu_link_clothes.click()
        self.menu_chapter.click()
        self.menu_subsection.click()
        self.choose_a_product.click()
        time.sleep(1)
        self.click_random_color()
        time.sleep(1)
        self.click_random_size()
        time.sleep(1)

        title = self.get_element_text(self.title_text)
        price = self.get_element_text(self.product_price_text)
        article = self.get_element_text(self.product_article_text)
        color = self.get_element_text(self.product_color_text)
        size = self.get_element_text(self.product_size_text)

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
        self.click(self.menu_link_clothes, " блок одежда")
        self.click(self.menu_chapter, " раздел Брюки")
        self.click(self.menu_subsection, " подраздел Легинсы")
        self.click(self.choose_a_product, "Выброр товара")
        self.click(self.add_favorite_btn, "Добавка в избранное")
        self.click(self.favorites_btn, " в избранное")
        self.click(self.choose_a_product_in_favorite, "выбор товара в избранном")

        # title = self.get_element_text(self.title_text)
        # price = self.get_element_text(self.product_price_text)
        # article = self.get_element_text(self.product_article_text)
        # color = self.get_element_text(self.product_color_text)
        # size = self.get_element_text(self.product_size_text)
        #
        # return title, price, article, color, size