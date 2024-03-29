import os
import time

import allure
import pytest

from pages.login import LoginPage
from pages.cart import CartPage
from pages.catalog import CatalogPage



@allure.feature("тесты корзины")
@pytest.mark.usefixtures("setup")
class TestBasket:

    @staticmethod
    @allure.title("Добавление в корзину с рандомным выбором цвета и размера")
    def test_add_to_basket():
        page = CatalogPage()
        title, price, article, color, size = page.add_to_basket()
        page.add_to_cart.click()
        time.sleep(2)
        page.basket_btn.click()
        page = CartPage()
        title_cart, price_cart, article_cart, color_cart, size_cart = page.get_cart_data()

        assert title == title_cart, print('Название товара в карточке и корзине отличаются')
        assert price == price_cart, print('Цена товара в карточке и корзине отличаются')
        assert article_cart in article, print('Артикул товара в карточке и корзине отличаются')
        assert color_cart in color, print('Цвет товара в карточке и корзине отличаются')
        assert size == size_cart, print('Размер товара в карточке и корзине отличаются')


    @staticmethod
    @allure.title("Добавление в корзину несколько товаров")
    def test_basket_multiple_products():
        page = CatalogPage()


        page.basket_multiple_products()
        time.sleep(2)
        page.basket_btn.click()
        time.sleep(2)
        page = CartPage()
        price_bags_cart, price_shoes_cart, quantity_products_cart, total_cost_products_cart, final_cost_products_cart, delivery_cart = page.get_cart_multidatabase()

        assert quantity_products_cart == "2", print(
            'Количество добавленных товаров в корзине не совпадает с количеством указанном в строке "количество"')
        assert int(price_bags_cart) + int(price_shoes_cart) == int(
            total_cost_products_cart), print(
            "Сумма добавленных товаров в корзине не совпадает с общей стоимостью товаров")
        assert int(price_bags_cart) + int(price_shoes_cart) + int(delivery_cart) == int(
            final_cost_products_cart), print(
            "Сумма добавленных товаров в корзине + стоимость доставки не равна итоговой стоимости товаров")
        assert int(total_cost_products_cart) + int(delivery_cart) == int(final_cost_products_cart), print(
            "Общая сумма + доставка не равна Итоговой сумме")

    @allure.step("Изменение количества товаров в корзине")
    def test_basket_changes_products(self):
        page = CatalogPage()
        price_belts = page.basket_changes_products()
        time.sleep(2)
        page.basket_btn.click()
        time.sleep(2)

        page = CartPage()
        page.basket_changes_products_in_cart()
        price_product_cart, choose_quantity, quantity_products_cart, final_cost_products_cart, total_information, total_cost_products_cart = page.get_quantity_products_and_final_cost()
        information_cart = choose_quantity + " X " + price_belts


        if choose_quantity != '1':
            assert information_cart in total_information, print(
                'Нужный текст "цена*количество товаров" не присутствует')

        assert choose_quantity == quantity_products_cart, print('Количество товаров в ,таблице где происходит смена количества товаров, и количество в итого не равно')
        assert int(price_belts) * int(quantity_products_cart) == int(final_cost_products_cart), print('Итоговая сумма не равна цене товара умноженная на количество товаров')






