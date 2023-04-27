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


class SmokePage(BasePage):
    # locators

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
