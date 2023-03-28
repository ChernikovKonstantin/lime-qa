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


@allure.feature("Тесты фильтрации")
@pytest.mark.usefixtures("setup")
class TestFilters:

    @allure.title("Тест цикла")
    @allure.link("https://lmdev.testrail.io")
    def test_cycle(self):

        page = LoginPage()
        page.authorization()
        page.click(page.close_btn, "Закрыть профиль")
        time.sleep(2)

        page = CatalogPage()
        page.click(page.hamburger_menu, "гамбургер-меню")
        time.sleep(2)
        page.click(page.menu_link_shoes, "раздел Обувь")
        time.sleep(2)
        page.click(page.menu_subsection_shoes, "подраздел Лоферы")
        time.sleep(2)

        page = FilterPage()
        page.click(page.button_filter, ' кнопка фильтра')
        page.cycle()




