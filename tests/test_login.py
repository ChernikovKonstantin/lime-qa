import os
import time

import allure
import pytest

from pages.account import AccountPage
from pages.home import HomePage
from pages.login import LoginPage


@allure.feature("Тесты логина")
@pytest.mark.usefixtures("setup")
class TestLogin():
    @staticmethod
    @allure.title("Успешный вход")
    def test_login_success():
        page = HomePage()
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()

        page = LoginPage()
        page.login(email=os.getenv("test_user"), password=os.getenv("password"))
        page.check_logout_btn_is_visible()

    @staticmethod
    @allure.title("Неуспешный вход")
    def test_login_fail():
        page = HomePage()
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()

        page = LoginPage()
        page.login(email="qwerty@qwerty.qwerty", password=os.getenv("password"))
        page.check_login_error()

    @staticmethod
    @allure.title("Регистрация")
    def test_registration_success():
        page = HomePage()

        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields()

        page = LoginPage()
        page.check_logout_btn_is_visible()

        time.sleep(3)
