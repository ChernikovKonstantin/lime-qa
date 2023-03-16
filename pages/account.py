import allure
from selene.api import s

from pages.base import BasePage


class AccountPage(BasePage):
    # Locators
    enter_btn = s(".btn.btn-block.btn-outline.btn-primary")
    #registration_btn = s(".btn.btn-block.btn-primary")


    # Methods
    @allure.step("Нажать Войти")
    def click_enter_btn(self):
        self.enter_btn.click()

    # @allure.step("Нажать Зарегистрироваться")
    # def click_registration_btn(self):
    #     self.registration_btn.click()


