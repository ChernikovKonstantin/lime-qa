import random
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

    @allure.step("Взять элемент в виде текста")
    def get_cart_data(self):
        title_cart = self.get_element_text(self.title_cart_text)
        price_cart = self.get_element_text(self.product_price_cart_text).lower()
        article_cart = self.get_element_text(self.product_article_cart_text)
        color_cart = self.get_element_text(self.product_color_cart_text).lower()
        size_cart = self.get_element_text(self.product_size_cart_text)
        return title_cart, price_cart, article_cart, color_cart, size_cart
