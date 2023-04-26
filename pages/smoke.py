import os
import time
import re

import allure
from selene.api import be, have, s
from selene.support.shared.jquery_style import ss

from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.login import LoginPage


class PaymentPage(BasePage):

    # locators main screen

    banners_main_page_image = ss("//div[@class='slide']")
    banner_main_page_image = s("//div[@class='slide']")
    banners_main_page_video = ss("//video")



    card_number_field = s("//input[@type='text' and @placeholder='Введите номер карты']")
    validity_period_field = s("//input[@type='text' and @placeholder='Дата окончания срока действия']")
    card_holder_field = s("//input[@type='text' and @placeholder='Владелец карты']")
    security_code_field = s("//input[@type='text' and @placeholder='Код безопасности CVV2']")
    promo_code_field = s("//input[@type='text' and @placeholder='Промокод']")
    to_pay_btn = s("//button[@class ='btn btn-block']")
    to_pay_btn_string = "//button[@class ='btn btn-block']"
    success_btn = s("//button[@class = 'button button_primary']")
    success_btn_string = "//button[@class = 'button button_primary']"
    success_btn_fault = s("//button[@class='button button_secondary']")
    success_btn_fault_string = "//button[@class='button button_secondary']"

    title_thank_you_page_text = s("//div[contains(text(),'Спасибо!')]")
    dropdown_quantity_product_on_payment = s("//div[@class='DropdownList__container DropdownList__inline']")
    # dropdown_quantity_product = s("(//div[@class='SvgIcon'])[2]/child::*")
    dropdown_quantity_product_select_5_on_payment = s("(//span[@class='DropdownList__title'])[5]")
    dropdown_quantity_product_select_1_on_payment = s("(//span[@class='DropdownList__title'])[1]")
    error_card_payment = s('// div[contains(text(), "ОПЛАТА НЕ ПРОШЛА: Свяжитесь с вашим банком или воспользуйтесь другой картой")]')
    error_card_payment_string = '// div[contains(text(), "ОПЛАТА НЕ ПРОШЛА: Свяжитесь с вашим банком или воспользуйтесь другой картой")]'

    #error_card_not_money = s('//div[contains(text(),"ОПЛАТА НЕ ПРОШЛА: Недостаточно средств на карте"]')
    error_card_not_money_string = '//div[@class="CustomerCartSummary__error"]'
    error_card_not_not_valid_card = '//div[contains (text(), "Неправильный номер карты")]'
    block_product = ss("//div[@class='CartTable__row']")
    message_out_of_stock = ss('//p[contains(text(), "Нет в наличии")]')
    button_del = s('//div[@class="SvgIcon IButtonIcon"]/child::*')
    button_del2 = s("//p[@class='CartTable__error']/ancestor::div[@class='CartTable__name']/following-sibling::button//div[@class='SvgIcon IButtonIcon']/child::*")

    @allure.step("Цикл проверки баннеров на гланом экране")
    def cycle_check_bunners(self):

        for i in range(len(self.banners_main_page_image)):


            url_main = self.get_url
            name_image = self.get_attribute(self.banners_main_page_image[i], 'style')
            self.click(self.banners_main_page_image[i], " баннер")
            url_catalog = self.get_url
            self.driver.back()










