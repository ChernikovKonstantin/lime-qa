import allure
from selene import query, be
from selene.api import browser
from selene.support.conditions.be import visible
from selene.support.shared import browser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    @allure.step("Получение атрибута")
    def get_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    @allure.step("Получение текущего url")
    def get_url(self):
        return browser.driver.current_url

    @allure.step("Перемещение к элементу")
    def move_to(self, element):
        driver = browser.driver
        action = ActionChains(driver)
        action.move_to_element(element).perform()

    @allure.step("Проверка наличия элемента")
    def wait_element(self, locator):
        browser.s(locator).should(be.visible)

    @allure.step("Проверка отсутсвия элемента")
    def wait_element_not_visible(self, locator):
        browser.s(locator).should_not(be.visible)

    @allure.step("Проверка наличия элемента")
    def wait_element_assure(self, element):
        element.assure(visible, 15)
        # wait = WebDriverWait(browser.driver, 10)
        # wait.until(EC.visibility_of((By.XPATH, element)))

    @allure.step("Сравнение значений {expression1} и {expression2}")
    def assert_check_expressions(self, expression1, expression2, allureText):
        assert expression1 == expression2, print(allureText)

    @allure.step("Проверка не соответсвия значений {expression1} и {expression2}")
    def assert_check_not_expressions(self, expression1, expression2, allureText):
        assert expression1 != expression2, print(allureText)

    @allure.step("Проверка наличия текста {expression1} в {expression2}")
    def assert_check_coincidence(self, expression1, expression2, allureText):
        assert expression1 in expression2, print(allureText)

    @allure.step("Проверка числового значения в пределах {value_from} в {value_to}")
    def assert_check_range(self, value_from, value_to, value_check,  allureText):
        assert value_check>=value_from and value_check <= value_to, print(allureText)

    @allure.step("Нажать Enter")
    def push_enter(self, element, fieldName):
        element.send_keys(Keys.ENTER)

    @allure.step("Нажать Backspace")
    def push_backspace(self, element, fieldName):
        element.send_keys(Keys.BACKSPACE)

    @allure.step("Очистить поле")
    def field_clear(self, element, fieldName):
        element.clear()



    @allure.step("Назад в браузере")
    def browser_back(self) -> object:
        browser.driver.back()






    @allure.step("Поиск количества одинаковых элементов")
    def search_same_elements(self, element):
        '''
        Docstring: выполнение поиска количества одинаковых элементов на странице
        :param element: локатор
        :return: количество элементов, число
        '''
        elements = browser.all(element)
        count = 0
        for element in elements:
            count += 1
            print(elements)

        return count












