import os
import time

import allure
import pytest

from pages.account import AccountPage
from pages.home import HomePage
from pages.login import LoginPage


@allure.feature("Тесты оплаты")
@pytest.mark.usefixtures("setup")
class TestPayment:


    @staticmethod
    @allure.title("Оплата с промокодом")
    def test_payment_promo():
        page = HomePage()
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()

        page = LoginPage()
        page.login(email=os.getenv("test_user"), password=os.getenv("password"))
        page.check_logout_btn_is_visible()