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

    #ОСНОВНОЙ ЭКРАН

    @allure.title("Главная страница")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=121",
                 "https://lmdev.testrail.io/index.php?/cases/view/852")
    def test_main_screen(self):
        page = SmokePage()
        page.cycle_banners()
        page.video()
        page.logo()

    @allure.title("Главная страница главное меню")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=121")
    def test_main_screen_main_menu(self):
        page = SmokePage()
        page.main_menu_search()
        #page.main_menu()


    @allure.title("Главная страница меню каталога")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=121")
    def test_main_screen_menu(self):
        page = SmokePage()
        page.catalog_menu_link()
        page.catalog_menu_parents_link_clothes()
        page.catalog_menu_parents_link_lingerie()
        page.catalog_menu_parents_link_accessories()
        page.catalog_menu_parents_link_shoes()
        page.catalog_menu_parents_link_special_offer()
        page.catalog_menu_parents_link_campaigns()

    # ПРОФИЛЬ

    @allure.title("Профиль пользователя")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=122")
    def test_profile(self):
        page = SmokePage()
        page.user_login_not_valid()
        page.click(page.button_close_screen, " закрыть экран входа\регистрации")
        page.user_login()
        page.user_registration_not_valid()
        page.user_registration_and_first_lk()
        page.user_profile_with_order()

    @allure.title("Экран поиска")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=123")
    def test_search(self):
        page = SmokePage()
        page.search_successful_text()
        page.search_successful_article()
        page.search_not_result()

    @allure.title("Оплата и оформление заказа")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=123")
    def test_payment(self):
        page = SmokePage()
        page.test_product_registration_cart_promo_code()






