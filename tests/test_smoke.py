import json
import os
import time
from this import s

import allure
import pytest
import requests
from pages.account import AccountPage
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.filters import FilterPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.payment import PaymentPage
from pages.smoke import SmokePage


@allure.feature("Смоук тест")
@pytest.mark.usefixtures("setup")
class TestSmoke:


    @allure.title("Главная страница")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=121")
    def test_main_screen(self):
        page = SmokePage()
        #page.cycle_banners()
        page.video()

