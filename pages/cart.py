import random
import re
import time

import allure
from selene.api import *

from pages.base import BasePage


class CartPage(BasePage):
    title_cart_text = s("//div[@class='CartTable__name']")
    product_price_cart_text = s("//div[@class='CartTable__cost']")
    product_article_cart_text = s("(//div[@class='CartTable__color']/p)[2]")
    product_color_cart_text = s("(//div[@class='CartTable__color']/p)[1]")
    product_size_cart_text = s("//div[@class='SizeSelector__selected']")
    product_bags_cart_text = s("(//div[@class='CartTable__cost']//span)[1]")
    product_shoes_cart_text = s("(//div[@class='CartTable__cost']//span)[2]")
    product_lingerie_cart_text = s("(//div[@class='CartTable__cost'])[3]")
    quantity_products_cart_text = s("//div[contains(text(),'Количество')]/following-sibling::div/span")
    total_cost_products_cart_text = s("//div[contains(text(),'Общая стоимость товаров')]/following-sibling::div/span")
    final_cost_products_cart_text = s("//div[contains(text(),'Итого')]/following-sibling::div/span")
    delivery_cart_text = s("//div[contains(text(),'Доставка')]/following-sibling::div/span")
    choose_quantity_in_cart = s("//div[@class='DropdownList__container DropdownList__inline']")
    random_quantity = ss("//span[@class= 'DropdownList__title']")
    choose_quantity_text = s("//div[@class='DropdownList__container DropdownList__inline']")
    price_product_text = s("(//div[@class='CartTable__cost'])//following-sibling::div/span[1]")
    total_information_text = s("//div[@class= 'CartTable__sum']")


    @allure.step("Получение данных корзины: заголовок, цена, артикул, цвет, размер ")
    def get_cart_data(self):
        title_cart = self.get_element_text(self.title_cart_text, 'Заголовок в корзине')
        price_cart = self.get_element_text(self.product_price_cart_text, 'Цена в корзине').lower()
        article_cart = self.get_element_text(self.product_article_cart_text, 'Артикул в корзине')
        color_cart = self.get_element_text(self.product_color_cart_text, 'Цвет в корзине').lower()
        size_cart = self.get_element_text(self.product_size_cart_text, 'Размер в корзине')
        return title_cart, price_cart, article_cart, color_cart, size_cart

    @allure.step(
        "Получение: цена товаров, количество добавленных продуктов, Общая стоимость товаров, стоимость доставки, итоговая стоимость")
    def get_cart_multidatabase(self):
        price_bags_cart = re.sub('[^0-9]', "",
                                 self.get_element_text(self.product_bags_cart_text, 'цена сумки в корзине'))
        price_shoes_cart = re.sub('[^0-9]', "",
                                  self.get_element_text(self.product_shoes_cart_text, 'цена туфли в корзине'))
        quantity_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.quantity_products_cart_text,
                                                                            'количество товаров в корзине'))
        total_cost_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.total_cost_products_cart_text,
                                                                              'общая стоимость товаров в корзине'))
        final_cost_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.final_cost_products_cart_text,
                                                                              'итоговая стоимость товаров в корзине'))
        delivery_cart = re.sub('[^0-9]', "", self.get_element_text(self.delivery_cart_text, 'цена доставки в корзине'))


        return price_bags_cart, price_shoes_cart, quantity_products_cart, total_cost_products_cart, final_cost_products_cart, delivery_cart

    @allure.step("Изменеие количества  товаров и проверка измененной общей стоимости")
    def basket_changes_products_in_cart(self):
        self.click(self.choose_quantity_in_cart, "Количество в корзине")
        self.click_random_quantity()


    @allure.step(
        "Получение: количество добавленных(рандомно) товаров, Количество товаров в итого, стоимость товара, итоговая стоимость")
    def get_quantity_products_and_final_cost(self):
        price_product_cart = re.sub('[^0-9]', "",
                                    self.get_element_text(self.price_product_text, 'цена товара в корзине'))

        choose_quantity = re.sub('[^0-9]', "",
                                 self.get_element_text(self.choose_quantity_text, 'выбор количества товаров в корзине'))

        time.sleep(2)
        quantity_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.quantity_products_cart_text,
                                                                            'количество товаров в корзине'))
        final_cost_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.final_cost_products_cart_text,
                                                                              'итоговая стоимость товаров в корзине'))
        total_information = ''
        if choose_quantity != '1':
            total_information = self.get_element_text(self.total_information_text,
                                                      'информация = цена*количество товаров')



        total_cost_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.total_cost_products_cart_text,
                                                                              'общая стоимость товаров в корзине'))
        return price_product_cart, choose_quantity, quantity_products_cart, final_cost_products_cart, total_information, total_cost_products_cart

    @allure.step("Рандомный выбор количества")
    def click_random_quantity(self):
        random.choice(self.random_quantity).click()

