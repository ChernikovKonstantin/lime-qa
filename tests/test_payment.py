import os
import time

import allure
import pytest

from pages.account import AccountPage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.home import HomePage
from pages.login import LoginPage


@allure.feature("Тесты оплаты")
@pytest.mark.usefixtures("setup")
class TestPayment:

    @allure.title("Покупка товара")
    def test_product_registration(self):
        page = LoginPage()
        page.authorization()
        page.click_close_btn()

        page = CatalogPage()
        page.basket_changes_products()
        page.basket_btn.click()

        page = LoginPage()
        page.click_making_an_order_btn()
        time.sleep(2)
        page = CartPage()
        page.filling_fields_registration_product()
        time.sleep(5)

    @allure.title("Оплта картой + валидный промокод")
    def test_product_registration(self):
            page = LoginPage()
            page.authorization()
            page.click_close_btn()

            page = CatalogPage()
            page.basket_changes_products()
            page.basket_btn.click()

            page = LoginPage()
            page.click_making_an_order_btn()
            time.sleep(2)
            page = CartPage()
            page.filling_fields_registration_product()
            time.sleep(5)



