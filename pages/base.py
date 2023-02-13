import allure
from selene import query
from selene.api import browser


class BasePage:
    @staticmethod
    def open_url(url):
        with allure.step(f"Открыть страницу {url}"):
            browser.open_url(url)

    def get_element_text(self, element):
        return element.get(query.text)
