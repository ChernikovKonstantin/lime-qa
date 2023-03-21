import os
import time

import allure
from selene.api import be, have, s

from pages.base import BasePage


class LoginPage(BasePage):

    # Locators
    email_input = s('input[placeholder="Введите e-mail"]')
    password_input = s('input[type="password"]')
    enter_btn = s('button[type="submit"]')
    logout_btn = s('//button[contains(.,"Выйти")]')
    error_message = s(".snack-bar")
    account_btn = s('a[href="/#lk"]')
    authorization_btn = s("//button[contains(text(),'Войти')]")
    close_btn = s("//button[@class = 'IButton IButtonClose ViewModal__closer']")
    product_price_text = s("//div[@class='product__price']")
    product_article_text = s("//div[@class='product__article']")
    product_color_text = s("//div[@class='ColorSelector product__colors']")
    product_size_text = s("//div[@class='SizeSelector__selected']")
    add_favorite_btn = s("//div[@class='actions__fav']")
    favorites_btn = s("//a[contains(@href,'#favorites') and @class='btn-control']")


    # Methods
    def login(self, email, password):
        with allure.step(f"Войти как '{email}' '{password}'"):
            self.email_input.set_value(email)
            self.password_input.set_value(password)
            self.enter_btn.should(be.enabled).click()

    @allure.step("Проверить что кнопка Выйти отображается")
    def check_logout_btn_is_visible(self):
        self.logout_btn.should(be.visible)

    @allure.step("Проверить что ошибка логина отображается")
    def check_login_error(self):
        self.error_message.should(have.text("Неверный логин или пароль"))

    @allure.step("Закрыть л.к")
    def click_close_btn(self):
        self.close_btn.click()

    @allure.step("Авторизации пользователя")
    def authorization(self):
        self.click(self.account_btn, "Нажать на Личный кабинет")
        self.click(self.authorization_btn, "Нажать Войти")
        self.set_text(self.email_input, os.getenv("test_user"), "Поле Email")
        self.set_text(self.password_input, os.getenv("password"), "Поле Пароль")
        self.click(self.authorization_btn, "Нажать Войти")










