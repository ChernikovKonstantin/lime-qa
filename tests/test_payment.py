import os
import time

import allure
import pytest

from pages.account import AccountPage
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
        page = LoginPage()
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
        page = LoginPage()
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

        page = LoginPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(2)
        page = PaymentPage()

        page = page.filling_fields_registration_product_promo_not_valid()

        .wait_element(.promo_code_error_string)
        page.wait_element(page.discount_string)
        page.wait_element(page.price_finally_block_cart_text_string)
        page.wait_element(page.icon_discount_percent_block_cart_text_string)

        page.wait_element(page.to_pay_btn_string)
        page.to_pay_btn.click()

