import os
import time
from typing import re

import allure
from selene.api import be, have, s

from pages.base import BasePage


class PaymentPage(BasePage):
    # locators

    card_number_field = s("//input[@type='text' and @placeholder='Введите номер карты']")
    validity_period_field = s("//input[@type='text' and @placeholder='Дата окончания срока действия']")
    card_holder_field = s("//input[@type='text' and @placeholder='Владелец карты']")
    security_code_field = s("//input[@type='text' and @placeholder='Код безопасности CVV2']")
    promo_code_field = s("//input[@type='text' and @placeholder='Промокод']")
    to_pay_btn = s("//button[@class ='btn btn-block']")
    success_btn = s("//button[@class = 'button button_primary']")
    title_thank_you_page_text = s("//div[contains(text(),'Спасибо!')]")

    # locators for promocode

    price_finally_block_cart_text = s("//span[@class='sale']") # цена с промо в блоке корзина
    icon_discount_percent_block_cart_text = s('//span[@class="percent"]') # иконка процента промо
    discount_string = '//div[contains(text(), " Скидка на заказ")]'# строка Скидка на заказ
    price_discount_text = s('(//div[@class="CustomerCartSummary__value"])[3]/span')# сумма скидки
    price_without_discount_text = s('(//div[@class="CustomerCartSummary__value"])[2]/span')# итоговая сумма без промокода
    price_finally_text = s('(//div[@class="CustomerCartSummary__value"])[2]/span')# Итого





    @allure.step('Заполнение полей при оформлении товара')
    def filling_fields_registration_product(self):
        time.sleep(2)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.to_pay_btn.click()
        self.success_btn.click()
        # title_thank_you_page = self.get_element_text(self.title_cart_text, 'Заголовок в корзине')

    @allure.step('Заполнение полей при оформлении товара при оплате картой+валидный')
    def filling_fields_registration_product_promo_valid(self):
        time.sleep(3)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.set_text(self.promo_code_field, "XHGFAH", "Промо код")

        # Проверка суммы корзины с промо



        price_finally_block_cart, price_without_discount, price_discount, price_finally = self.sum_order_with_promo()

        assert (round((int(price_without_discount[:-5])),-1)) == (round((int(price_finally_block_cart[:-5])),-1)) + \
               (round((int(price_discount[:-5])),-1)), print('Ошибка проверки: цена с промо в блоке корзина + сумма скидки = итого')

        print(price_without_discount)


        print("end")


        time.sleep(2)

        self.to_pay_btn.click()
        time.sleep(2)
        self.success_btn.click()
        time.sleep(2)
        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, '')

        return title_thank_you_page

    def sum_order_with_promo(self):

        self.wait_element(self.discount_string)
        price_finally_block_cart = self.get_element_text(self.price_finally_block_cart_text, '')
        #price_without_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Цена без промо')))), -1)
        price_without_discount = self.get_element_text(self.price_without_discount_text, 'Цена без промо')
        price_discount  = self.get_element_text(self.price_discount_text , '')
        price_finally = self.get_element_text(self.price_finally_text, '')

        return price_finally_block_cart, price_without_discount, price_discount, price_finally

