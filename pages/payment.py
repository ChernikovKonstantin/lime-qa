import os
import time

import allure
from selene.api import be, have, s

from pages.base import BasePage


class PaymentPage(BasePage):

    card_number_field = s("//input[@type='text' and @placeholder='Введите номер карты']")
    validity_period_field = s("//input[@type='text' and @placeholder='Дата окончания срока действия']")
    card_holder_field = s("//input[@type='text' and @placeholder='Владелец карты']")
    security_code_field = s("//input[@type='text' and @placeholder='Код безопасности CVV2']")
    to_pay_btn = s("//button[@class ='btn btn-block']")
    success_btn = s("//button[@class = 'button button_primary']")
    title_thank_you_page_text = s("")

    @allure.step('Заполнение полей при оформлении товара')
    def filling_fields_registration_product(self):
        time.sleep(2)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.to_pay_btn.click()
        self.success_btn.click()
        title_thank_you_page = self.get_element_text(self.title_cart_text, 'Заголовок в корзине')

    @allure.step('Заполнение полей при оформлении товара при оплате картой+валидный промокод')
    def filling_fields_registration_product_(self):
        time.sleep(2)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.to_pay_btn.click()
        self.success_btn.click()
        title_thank_you_page = self.get_element_text(self.title_cart_text, 'Заголовок в корзине')