import os
import time

import allure
import pytest

from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage


@allure.feature("тесты корзины")
@pytest.mark.usefixtures("setup")
class TestBasket:

    @staticmethod
    @allure.title("Добавление в корзину")
    def test_add_to_basket():
        page = CatalogPage()
        title, price, article, color, size = page.add_to_basket()
        page.add_to_cart.click()
        time.sleep(5)
        page.basket_btn.click()
        page = CartPage()
        title_cart, price_cart, article_cart, color_cart, size_cart = page.get_cart_data()

        assert title == title_cart, print('Название товара в карточке и корзине отличаются')
        assert price == price_cart, print('Цена товара в карточке и корзине отличаются')
        assert article_cart in article, print('Артикул товара в карточке и корзине отличаются')
        assert color_cart in color, print('Цвет товара в карточке и корзине отличаются')
        assert size == size_cart, print('Размер товара в карточке и корзине отличаются')
        time.sleep(1)


    @staticmethod
    @allure.title("Добавление в корзину несколько товаров")
    def test_basket_multiple_products():
        page = CatalogPage()
        price_lingerie, price_shoes, price_bags  = page.basket_multiple_products()
        # print(price_lingerie, price_shoes, price_bags)

        time.sleep(2)
        page.basket_btn.click()
        time.sleep(1)
        page = CartPage()
        price_bags_cart, price_shoes_cart, price_lingerie_cart, quantity_products_cart, total_cost_products_cart, final_cost_products_cart, delivery_cart = page.get_cart_multidatabase()


        assert quantity_products_cart == "3", print('Количество добавленных товаров в корзине не совпадает с количеством указанном в строке "количество"')
        assert int(price_bags_cart) + int(price_shoes_cart) + int(price_lingerie_cart) == int(total_cost_products_cart), print ("Сумма добавленных товаров в корзине не совпадает с общей стоимостью товаров")
        assert int(price_bags_cart) + int(price_shoes_cart) + int(price_lingerie_cart) + int(delivery_cart) == int(final_cost_products_cart), ("Сумма добавленных товаров в корзине + стоимость доставки не равна итоговой стоимости товаров")
        assert int(total_cost_products_cart) + int(delivery_cart) == int(final_cost_products_cart), ("Общая сумма + доставка не равна Итоговой сумме")









