from pages.base import BasePage
from selene.api import s
import allure


class HomePage(BasePage):

    # Locators
    account_btn = s('a[href="/#lk"]')

    # Methods
    @allure.step("Нажать Аккаунт")
    def click_account_btn(self):
        self.account_btn.click()