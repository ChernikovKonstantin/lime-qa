import random
from random import randint

import allure
from selene.api import *

from pages.base import BasePage


class HomePage(BasePage):
    # Locators
    account_btn = s('a[href="/#lk"]')
    registration_btn = s("//button[contains(text(),'Зарегистрироваться')]")
    email_field = s("//input[@type='email' and @placeholder='E-mail']")
    phone_number_field = s("//input[@class= 'vti__input']")
    name_field = s("//input[@placeholder='Ваше имя']")
    surname_name_field = s("//input[@placeholder='Фамилия']")
    new_password_field = s("//input[@placeholder='Новый пароль']")
    repeat_the_password_field = s("//input[@placeholder='Повторите пароль']")



    # Methods
    @allure.step("Нажать Аккаунт")
    def click_account_btn(self):
        self.account_btn.click()

    @allure.step("Нажать Зарегистрироваться")
    def click_registration_btn(self):
        self.registration_btn.click()

    @allure.step("Заполнение всех полей регистрации")
    def fill_registration_fields(self):
        self.email_field.set_value('test' + str(randint(0, 9999)) + '@test.ru')
        self.phone_number_field.set_value('+79998887755')
        self.name_field.set_value('Test')
        self.surname_name_field.set_value('Testerov')
        self.new_password_field.set_value('123456789')
        self.repeat_the_password_field.set_value('123456789')
        self.registration_btn.click()


