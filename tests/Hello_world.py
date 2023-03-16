
import time

import allure
import pytest

from pages.home import HomePage
from pages.login import LoginPage


@allure.feature("тесты на время проблемы с login default")
@pytest.mark.usefixtures("setup")
class TestHelloWorld:

    @staticmethod
    @allure.title("Регистрация без чек-бокса рассылки")
    def test_registration_none_mailing():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields()
        time.sleep(10)
        page = LoginPage()
        page.check_logout_btn_is_visible()

        #тест пуша2