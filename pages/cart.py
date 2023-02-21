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
    product_bags_cart_text = s("(//div[@class='CartTable__cost'])[1]")
    product_shoes_cart_text = s("(//div[@class='CartTable__cost'])[2]")
    product_lingerie_cart_text = s("(//div[@class='CartTable__cost'])[3]")
    quantity_products_cart_text = s("//div[contains(text(),'Количество')]/following-sibling::div/span")
    total_cost_products_cart_text = s("//div[contains(text(),'Общая стоимость товаров')]/following-sibling::div/span")
    final_cost_products_cart_text = s("//div[contains(text(),'Итого')]/following-sibling::div/span")
    delivery_cart_text = s("//div[contains(text(),'Доставка')]/following-sibling::div/span")

    @allure.step("Получение данных корзины: заголовок, цена, артикул, цвет, размер ")
    def get_cart_data(self):
        title_cart = self.get_element_text(self.title_cart_text)
        price_cart = self.get_element_text(self.product_price_cart_text).lower()
        article_cart = self.get_element_text(self.product_article_cart_text)
        color_cart = self.get_element_text(self.product_color_cart_text).lower()
        size_cart = self.get_element_text(self.product_size_cart_text)
        return title_cart, price_cart, article_cart, color_cart, size_cart

    @allure.step(
        "Получение: цена товаров, количество добавленных продуктов, Общая стоимость товаров, стоимость доставки, итоговая стоимость")
    def get_cart_multidatabase(self):
        price_bags_cart = re.sub('[^0-9]', "", self.get_element_text(self.product_bags_cart_text))
        price_shoes_cart = re.sub('[^0-9]', "", self.get_element_text(self.product_shoes_cart_text))
        price_lingerie_cart = re.sub('[^0-9]', "", self.get_element_text(self.product_lingerie_cart_text))
        quantity_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.quantity_products_cart_text))
        total_cost_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.total_cost_products_cart_text))
        final_cost_products_cart = re.sub('[^0-9]', "", self.get_element_text(self.final_cost_products_cart_text))
        delivery_cart = re.sub('[^0-9]', "", self.get_element_text(self.delivery_cart_text))

        return price_bags_cart, price_shoes_cart, price_lingerie_cart, quantity_products_cart, total_cost_products_cart, final_cost_products_cart, delivery_cart
