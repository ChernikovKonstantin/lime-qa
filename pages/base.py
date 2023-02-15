import allure
from selene import query
from selene.api import browser


class BasePage:
    @staticmethod
    def open_url(url):
        with allure.step(f"Открыть страницу {url}"):
            browser.open_url(url)

    @allure.step("Взять текст")
    def get_element_text(self, element):
        return element.get(query.text)

    @allure.step("Заполнение поля {fieldName} текстом '{text}'")
    def set_text(self, element, text, fieldName):
        element.set_value(text)
    @allure.step("Клик по элементу {text}")
    def click(self, element, text):
        element.click()

    @allure.step("Получение аттрибута")
    def get_attribute(self, element, attribute):
        return element.get_attribute(attribute)

