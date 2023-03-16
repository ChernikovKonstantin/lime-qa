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
        self.set_text(self.email_field, 'test' + str(randint(0, 9999)) + '@test.ru', " почта")
        self.set_text(self.phone_number_field, "+79998887755", " номер телефона")
        self.set_text(self.name_field, "Test", " ИМЯ")
        self.set_text(self.surname_name_field, "Testerov", " ФАМИЛИЯ")
        self.set_text(self.new_password_field, "123456789", " НОВЫЙ ПАРОЛЬ")
        self.set_text(self.repeat_the_password_field, "123456789", " ПОДТВЕРДИТЕ ПАРОЛЬ")
        self.registration_btn.click()



