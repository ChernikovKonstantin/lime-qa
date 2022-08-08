import allure
from selene.api import browser


class BasePage:

    @staticmethod
    def open_url(url):
        with allure.step(f"Открыть страницу {url}"):
            browser.open_url(url)
