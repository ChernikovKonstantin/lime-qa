import os
import time

import allure
import pytest

from pages.account import AccountPage
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.payment import PaymentPage


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
        page = CartPage()
        page.click_making_an_order_btn()
        time.sleep(2)
        page = PaymentPage()
        message = page.filling_fields_registration_product()
        assert message == "СПАСИБО!", print('Нужный текст "СПАСИБО" не присутствует')
        page.filling_fields_registration_product()
        time.sleep(5)

    @allure.title("Оплата картой + валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/441")
    def test_product_registration_cart_promo_code(self):
        page = LoginPage()
        page.authorization()
        page.click_close_btn()
        page = CatalogPage()
        page.basket_changes_products()
        page.basket_btn.click()
        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(2)
        page = PaymentPage()
        title_thank_you_page = page.filling_fields_registration_product_promo_valid()
        print(title_thank_you_page)

        assert title_thank_you_page == "СПАСИБО!", print("Ошибка сообщения. Текст ошибки: " + title_thank_you_page)


    @allure.title("Оплата картой +  не валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/443")
    def test_product_registration_cart_promo_code(self):
        page = LoginPage()
        page.authorization()
        page.click_close_btn()

        page = CatalogPage()
        page.basket_changes_products()
        page.basket_btn.click()

        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(2)
        page = PaymentPage()

        page.filling_fields_registration_product_promo_not_valid()

    @allure.title("Проверка сравнения двух значений отображением шагах в аллюр")
    def test_assert(self):

        page = PaymentPage()
        exp1 = 5
        exp2 = 4
        page.assert_check_expressions(exp1, exp2, 'текст в ассерте')

    @allure.title("Оплата картой заказа суммой более 6000 с формированием заказа в корзине")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/442&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=80")
    def test_product_discount_cart_6000(self):
        page = LoginPage()
        page.authorization()
        page.click_close_btn()

        page = CatalogPage()
        page.basket_changes_products_1399()
        page.basket_btn.click()
        time.sleep(1)

        page = CartPage()

        page.change_value_products_in_cart()
        time.sleep(3)
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(1)

        page = PaymentPage()
        page.sum_order_with_discount_6000()
        page.change_value_products_in_payment_1_unit()
        page.check_wait_message_without_discount()
        page.change_value_products_in_payment_5_unit()
        page.sum_order_with_discount_6000()

        page.filling_fields_registration_product()
        self.to_pay_btn.click()
        time.sleep(2)
        self.success_btn.click()
        time.sleep(2)
        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, '')
        assert title_thank_you_page == "СПАСИБО!", print("Ошибка сообщения. Текст ошибки: " + title_thank_you_page)















