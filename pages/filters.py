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

        #checkbox_block_price = s('//span[contains (text(), "000")]') //span[contains (text(), "000")]/../input
        checkbox_block_price = s('//span[contains (text(), "000")]/../input')
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



        # @allure.step("Json параметров фильтров по типу товара Лоферы ")
        # def type_filters(self):
            # URL для DEV
            #base_url = os.getenv('base_url')[:8] + os.getenv('base_url')[
             #                                      21:] + 'api/section/filters/loafers'
            # base_url = os.getenv('base_url') + 'api/section/filters/loafers'
            # response_type_filter = requests.get(base_url)
            #
            # return response_type_filter.json()

        # @allure.step("Цикл перебора цветов фильтра Лоферы ")
        # def cycle_check_bocks_color(self):
        #     # for i in range(len(self.elements_block_color)):
        #     self.click(self.elements_block_color[i], " чекбокс выбора цвета")
        #     time.sleep(5)
        #     color_filter = self.get_element_text(self.element_block_color, ' цвет чекбокса фильтра').lower()
        #     self.click(self.elements_block_color[i], " чекбокс выбора цвета")
        #     return color_filter

        @allure.step("Получение статуса чекбокса ")
        def get_checkbox_status(self):
            return self.get_attribute(self.checkbox_block_color_attrib, 'value')

        # @allure.step("Цикл перебора разделов меню")
        # def cycle_menu(self):
        #     for i in range
        #         page = CatalogPage()
        #         page.click(page.hamburger_menu, "гамбургер-меню")
        #         page.click(page.menu_section_shoes, "раздел Обувь")
        #         page.click(page.menu_subsection_shoes_lofers, "подраздел Лоферы")

        @allure.step("Цикл запросов типа фильтра ")
        def cycle_type_filters(self):
            base_url = os.getenv('base_url') + 'api/section/filters/boots'
            response_type_filter = requests.get(base_url).json()
            type_filter = list(response_type_filter.keys())


            # for i in range(len(response_type_filter['colors'])):
            #     filter_color_id = str(response_type_filter['colors'][i]['id'])
            #     filter_color_name = str(response_type_filter['colors'][i]['name'])
            #
            #     url_color = os.getenv('base_url') + 'api/section/apply/boots' + '?' + type_filter[0][:-1] + '=' + filter_color_id
            #     request_color = requests.get(url_color).json()
            #
            #     status_checkbox = self.get_attribute(self.checkbox_block_color_attrib, 'value')
            #     if status_checkbox == "true":
            #         self.click(self.elements_block_color[i - 1], ' сброс состояния чекбокса')
            #     self.click(self.elements_block_color[i], " чекбокс выбора цвета")
            #
            #     time.sleep(2)
            #
            #     for i in range(len(request_color['items'][0]['cells'])):
            #         filter_color_name_product = self.get_element_text(self.cards_product_color_string_filter[i], ' название товара').capitalize()
            #
            #         filter_color_json = request_color['items'][0]['cells'][i]['entity']['models'][0]['color']['name']
            #         time.sleep(2)
            #         filter_color_name_product_json = request_color['items'][0]['cells'][i]['entity']['name']
            #         time.sleep(2)
            #
            #         page = BasePage()
            #         page.assert_check_coincidence(filter_color_name, filter_color_json, ' цвет товара в фильтре не соответсвует цвету товара в запросе api')
            #         page.assert_check_expressions(filter_color_name_product_json, filter_color_name_product, ' имя товара не соответствует цвету')
            #
            #         page = FilterPage()

            for i in range(len(response_type_filter['prices'])):
                filter_price_name = str(response_type_filter['prices'][i]['name'])
                filter_price_from = str(response_type_filter['prices'][i]['from'])
                filter_price_to = str(response_type_filter['prices'][i]['to'])

                url_color = os.getenv('base_url') + 'api/section/apply/boots' + '?' + type_filter[1][:-1] + '[]' + '=' + filter_price_from + ',' + filter_price_to
                request_price = requests.get(url_color).json()

                status_checkbox_price = self.get_attribute(self.checkbox_block_price, 'value')
                if status_checkbox_price == "true":
                    self.click(self.elements_block_color[i - 1], ' сброс состояния чекбокса')
                self.click(self.elements_block_color[i], " чекбокс выбора цвета")

                time.sleep(2)

                for i in range(len(request_color['items'][0]['cells'])):
                    filter_color_name_product = self.get_element_text(self.cards_product_color_string_filter[i], ' название товара').capitalize()

                    filter_color_json = request_color['items'][0]['cells'][i]['entity']['models'][0]['color']['name']
                    time.sleep(2)
                    filter_color_name_product_json = request_color['items'][0]['cells'][i]['entity']['name']
                    time.sleep(2)

                    page = BasePage()
                    page.assert_check_coincidence(filter_color_name, filter_color_json, ' цвет товара в фильтре не соответсвует цвету товара в запросе api')
                    page.assert_check_expressions(filter_color_name_product_json, filter_color_name_product, ' имя товара не соответствует цвету')

                    page = FilterPage()









