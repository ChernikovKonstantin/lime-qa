import os

import allure
import pytest

from pages.login import LoginPage
from pages.account import AccountPage
from pages.home import HomePage


@allure.feature("Тесты логина")
@pytest.mark.usefixtures("setup")
class TestLogin:
    @allure.title("Успешный вход")
    def test_login_success(self):
        page = HomePage()
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()

        page = LoginPage()
        page.login(email=os.getenv("test_user"), password=os.getenv("password"))
        page.check_logout_btn_is_visible()

    @allure.title("Неуспешный вход")
    def test_login_fail(self):
        page = HomePage()
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()

        page = LoginPage()
        page.login(email="qwerty@qwerty.qwerty", password=os.getenv("password"))
        page.check_login_error()
