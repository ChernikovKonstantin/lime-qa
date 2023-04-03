import os
import time
import re

import allure
import requests

from selene import driver
from selene.api import be, have, s
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss


import json
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.login import LoginPage


class FilterPage(BasePage):

        # locators

        # locators shoes

        #button_filter = s('//span[@class = "filter-button__title"]')
        button_filter = s('// span[contains(text(), "Фильтры")]')
        button_filter_string = '// span[contains(text(), "Фильтры")]'
        button_filter_closed = s('//button[@class = "IButton IButtonClose filter__closer"]')
        block_color = s("//div[@class='filter-group__options columns']")
        elements_block_color = ss('//div[@class="filter-group__options columns"]//span[@class="checkbox__text"]')
        element_block_color = s('//div[@class="filter-group__options columns"]//span[@class="checkbox__text"]')
        checkbox_block_color = s('//div[@class="filter-group__options columns"]//span[@class="checkbox__indicator"]')
        checkbox_block_color_attrib = s('//input[@class = "checkbox__element"]')
        cards_product_in_result_search = ss('//img[@class]')
        card_product_in_result_search = s('//img[@class]')
        card_product_color_string = s('//div[@class= "ColorSelector__title"]')
        cards_product_color_string_filter = ss('//div[@class = "CatalogProduct__title"]/child::*')
        card_product_color_string_filter = s('//div[@class = "CatalogProduct__title"]/child::*')



        @allure.step("Проверка возврата к результатам фильтра из карточки товара")

        @allure.step("Цикл проверки цвета")
        def cycle(self):
            for i in range(len(self.elements_block_color)):
                self.click(self.elements_block_color[i], " чекбокс выбора цвета")
                color_filter = self.get_element_text(self.element_block_color, ' цвет чекбокса фильтра')
                self.click(self.button_filter_closed, " кнопка закрытия фильтра")
                for y in range(len(self.cards_product_in_result_search)):
                    self.click(self.cards_product_in_result_search[y], " карточка товара")
                    color_card_text = self.get_element_text(self.card_product_color_string, 'цвет в карточке товара')
                    color_card = color_card_text[6:].upper()
                    self.assert_check_expressions(color_filter, color_card, ' цвет не соответствует')
                    browser.driver.back()
                self.click(self.button_filter, ' кнопка фильтра')

        @allure.step("Json_установленного фильтра")
        def filter_json(self):

            base_url = os.getenv('base_url')[:8]+os.getenv('base_url')[21:] + 'api/section/apply/all_shoes' + '?color=19'
            response = requests.get(base_url)

            return response.json()



        @allure.step("Json параметров фильтров по типу товара Лоферы ")
        def type_filters(self):
            base_url = os.getenv('base_url')[:8] + os.getenv('base_url')[
                                                   21:] + 'api/section/filters/loafers'

            response_type_filter = requests.get(base_url)

            return response_type_filter.json()

        @allure.step("Цикл перебора цветов фильтра Лоферы ")
        def cycle_check_bocks_color(self):
            # for i in range(len(self.elements_block_color)):
            self.click(self.elements_block_color[i], " чекбокс выбора цвета")
            time.sleep(5)
            color_filter = self.get_element_text(self.element_block_color, ' цвет чекбокса фильтра').lower()
            self.click(self.elements_block_color[i], " чекбокс выбора цвета")
            return color_filter

        @allure.step("Получение статуса чекбокса ")
        def get_checkbox_status(self):
            return self.get_attribute(self.checkbox_block_color_attrib, 'value')










