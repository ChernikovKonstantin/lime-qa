import os
import time

import allure
import pytest

from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.login import LoginPage


@allure.feature("тесты избранного")
@pytest.mark.usefixtures("setup")
class TestFavorites:

    @staticmethod
    @allure.title("Добавление в избранное")
    def test_add_to_favorites():
        page = LoginPage()
        page.authorization()

        page = CatalogPage()
        page.add_to_favorite()
        time.sleep(2)

        # title, price, article, color, size = page.add_to_basket()
        # page.favorites_btn.click()
        time.sleep(2)

        # assert title == title_cart, print('Название товара в карточке и корзине отличаются')
        # assert price == price_cart, print('Цена товара в карточке и корзине отличаются')
        # assert article_cart in article, print('Артикул товара в карточке и корзине отличаются')
        # assert color_cart in color, print('Цвет товара в карточке и корзине отличаются')
        # assert size == size_cart, print('Размер товара в карточке и корзине отличаются')
