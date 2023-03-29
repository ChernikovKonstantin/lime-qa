import os
import time
from this import s

import allure
import pytest

from pages.account import AccountPage
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.filters import FilterPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.payment import PaymentPage


@allure.feature("Тесты фильтров")
@pytest.mark.usefixtures("setup")
class TestFilters:

    @allure.title("Тест цикла проверки цвета Лоферов")
    @allure.link("https://lmdev.testrail.io")
    def test_cycle(self):

        page = LoginPage()
        page.authorization()
        page.click(page.close_btn, "Закрыть профиль")
        time.sleep(2)

        page = CatalogPage()
        page.click(page.hamburger_menu, "гамбургер-меню")
        page.click(page.menu_link_shoes, "раздел Обувь")
        page.click(page.menu_subsection_shoes, "подраздел Лоферы")

        page = FilterPage()
        page.wait_element(page.button_filter_string)
        time.sleep(1)
        page.click(page.button_filter, ' кнопка фильтра')
        time.sleep(3)
        page.cycle()
    @allure.title("Тест фильтра по АПИ")
    @allure.link("https://lmdev.testrail.io")
    def test_api(self):
        #page = LoginPage()
        #page.authorization()

        page = FilterPage()
        response = page.rest_api()
        print(response)



