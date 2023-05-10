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

    @allure.title("Оплата карта + валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/903")
    def test_payment_cart_valid_promo(self):
        page = PaymentPage()
        page.preview_payment()
        # page.enter_valid_promo()
        # page.cycle_type_promo_code()
        page.set_text(page.promo_code_field, "XHGFAH", "Промо код")
        page.sum_order_with_discount()
        page.pay_order()

    @allure.title("Оплата карта + валидный промокод, несколько товаров")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/904")
    def test_payment_cart_valid_promo_many_prducts(self):
        page = PaymentPage()
        page.preview_payment_many_products()
        page.set_text(page.promo_code_field, "XHGFAH", "Промо код")
        page.sum_order_with_discount_many()
        page.pay_order()

    @allure.title("Оплата карта + не валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/905")
    def test_payment_cart_valid_promo_many_prducts(self):
        page = PaymentPage()
        page.preview_payment()
        page.set_text(page.promo_code_field, "00000", "Промо код")
        page.check_payment_promo_not_valid()

    @allure.title("Проверка скидки при безналичной оплате на сайте заказа суммой > 6000")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/906&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=124")
    def test_payment_cart_order_more_6000(self):
        page = PaymentPage()
        page.preview_payment_6000()
        page.sum_order_with_discount()
        page.change_value_products_in_payment_1_unit()
        page.check_without_discount()
        page.change_value_products_in_payment_5_unit()
        page.sum_order_with_discount()
        page.pay_order()

    @allure.title("Проверка применения промокодов для заказов 6000 < Σ < 6000")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/907")
    def test_payment_promocodes_6000_sum_6000(self):
        page = PaymentPage()
        page.preview_payment_6000()
        page.enter_valid_promo_0()
        page.sum_order_with_discount()
        page.enter_valid_promo_10()
        page.sum_order_with_discount()
        page.enter_valid_promo_25()
        page.sum_order_with_discount()
        page.change_value_products_in_payment_1_unit()
        page.enter_valid_promo_0()
        page.check_without_discount()

    @allure.title("Оплата картой ошибка оплаты")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/908")
    def test_payment_card_error(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_courier, "Выбор типа доставки Курьер")
        page.click(page.type_of_payment_card, "Выбор типа оплаты Карта")
        page.pay_order_error()

    @allure.title("Оплата при получении, доставка курьером")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/912")
    def test_pay_receiving_courier(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_courier, 'Выбор типа доставки Доставка курьером')
        page.click(page.type_of_payment_receiving, 'Выбор типа оплаты При получении')
        page.wait_element_not_visible(page.string_data_card)
        page.pay_order_post_payment()



    @allure.title("Оплата банковской картой самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/913")
    def test_card_self(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')
        page.pay_order()

    @allure.title("Оплата банковской картой (недостаточно средств), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/914")
    def test_card_self_no_many(self):
        page = PaymentPage()
        page.preview_payment()
        page.set_text(page.card_number_field, "4012 8888 8888 1881", " тестовый номер карты  с ошибкой Недостаточно средств")
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')
        page.wait_element_assure(self.to_pay_btn)
        page.click(self.to_pay_btn, "кнопка оплаты")

        #нужно разобраться - можно ли перекидывать на сторонний сервис?
        page.wait_element(page.error_card_not_money_string)




























