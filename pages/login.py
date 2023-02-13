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
        # self.logout_btn.should_not(be.visible)

    # @allure.step("Проверить что товар добавлен в корзину")
    # def check_add_to_basket(self):
    #     self.logout_btn.should(be.visible)