import os
import time
import re

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
    to_pay_btn_string = "//button[@class ='btn btn-block']"
    success_btn = s("//button[@class = 'button button_primary']")
    title_thank_you_page_text = s("//div[contains(text(),'Спасибо!')]")

    # locators for promocode

    price_finally_block_cart_text = s("//span[@class='sale']") # цена с промо в блоке корзина
    price_finally_block_cart_text_string = "//span[@class='sale']"
    icon_discount_percent_block_cart_text = s('//span[@class="percent"]') # иконка процента промо
    icon_discount_percent_block_cart_text_string = '//span[@class="percent"]'
    discount_string = '//div[contains(text(), " Скидка на заказ")]'# строка Скидка на заказ
    price_discount_text = s('(//div[@class="CustomerCartSummary__value"])[3]/span')# сумма скидки
    price_without_discount_text = s('(//div[@class="CustomerCartSummary__value"])[2]/span')# итоговая сумма без промокода
    price_finally_text = s('(//div[@class="CustomerCartSummary__value"])[5]/span')# Итого
    promo_code_error_string = "//div[contains(text(), 'промокод не найден')]"  #ошибка промокода






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

    @allure.step('Проверка при оплате картой + валидный промо')
    def filling_fields_registration_product_promo_valid(self):
        time.sleep(3)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.set_text(self.promo_code_field, "XHGFAH", "Промо код")

        # Проверка суммы корзины с промо

        price_finally_block_cart, price_without_discount, price_discount, \
            price_finally, icon_discount_percent_block_cart, price_discount_icon = self.sum_order_with_promo()

        assert price_without_discount == price_finally + price_discount, \
            print('Ошибка проверки: цена с промо  + сумма скидки = итого')

        assert price_without_discount == price_finally_block_cart + price_discount, \
            print('Ошибка проверки: цена с промо в блоке корзина + сумма скидки = итого')

        assert price_finally_block_cart == price_without_discount - price_discount_icon, \
            print('Ошибка проверки: цена с промо в блоке корзина =  итого х %промо')
        #(round((int(price_without_discount[:-5])), -1))

        time.sleep(2)
        self.to_pay_btn.click()
        time.sleep(2)
        self.success_btn.click()
        time.sleep(2)
        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, '')

        return title_thank_you_page

    def sum_order_with_promo(self):

        self.wait_element(self.discount_string)
        price_finally_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_block_cart_text, 'Получение итоговой суммы заказа из блока Корзина'))))
        #price_without_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Цена без промо')))), -1)
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промокода'))))
        price_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text, 'Сумма скидки по промокоду, с округлением в большую сторону')))), -1)
        price_finally = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text, 'Получение итоговой суммы заказа'))))
        icon_discount_percent_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.icon_discount_percent_block_cart_text, 'Получение процента скидки'))))
        price_discount_icon = round(price_without_discount*(icon_discount_percent_block_cart/100), -1)

        return price_finally_block_cart, price_without_discount, price_discount, price_finally, icon_discount_percent_block_cart, price_discount_icon

    @allure.step('Проверка при оплате картой + не валидный промо')
    def filling_fields_registration_product_promo_not_valid(self):
        time.sleep(3)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.set_text(self.promo_code_field, "000000", "Не валидный Промокод")