import allure
from selene import query
from selene.api import browser
from selene.support.shared import browser
from selenium.webdriver import ActionChains


class BasePage:
    @staticmethod
    def open_url(url):
        with allure.step(f"Открыть страницу {url}"):
            browser.open_url(url)

    @staticmethod
    def open_url2(url):
        with allure.step(f"Открыть страницу {url}"):
            browser.open_url(url)

    @allure.step("Взять текст из элемента '{allureText}'")
    def get_element_text(self, element, allureText):
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

    @allure.step("Получение аттрибута")
    def get_url(self):
        return browser.driver.current_url

    @allure.step("Получение аттрибута")
    def move_to(self, element):
        driver = browser.driver
        action = ActionChains(driver)
        action.move_to_element(element).perform()

    @allure.step("Проверка отсутсвия элемента")
    def wait_element_not_visible(self, locator):
        browser.s(locator).should_not(be.visible)

    @allure.step("Проверка наличия элемента")
    def wait_element(self, locator):
        browser.s(locator).should(be.visible)



