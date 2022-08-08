import allure
from selene.api import s

from pages.base import BasePage


class HomePage(BasePage):

    # Locators
    account_btn = s('a[href="/#lk"]')

    # Methods
    @allure.step("Нажать Аккаунт")
    def click_account_btn(self):
        self.account_btn.click()
