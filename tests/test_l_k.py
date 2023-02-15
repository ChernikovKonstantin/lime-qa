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
        page.click_close_btn()
        time.sleep(1)
        page = CatalogPage()
        page.add_to_favorite()

    @staticmethod
    @allure.title("Добавление в избранное из каталога")
    def test_add_to_favorites_in_catalog():
        page = LoginPage()
        page.authorization()
        page.click_close_btn()
        time.sleep(1)



