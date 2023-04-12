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

    checkbox_block_color = s("//div[@class='filter-group__title' and contains (text(), 'Цвет')]/following-sibling::div//span[@class='checkbox__text']")
    checkboxes_block_color_attrib = ss("//div[@class='filter-group__title' and contains (text(), 'Цвет')]/following-sibling::div//input")
    checkboxes_block_color_click = ss ("//div[@class='filter-group__title' and contains (text(), 'Цвет')]/following-sibling::div//span[@class='checkbox__indicator']")

    #checkbox_block_price = s('//span[contains (text(), "000")]') //span[contains (text(), "000")]/../input
    checkboxes_block_price_attrb = ss("//div[@class='filter-group__title' and contains (text(), 'Цена')]/following-sibling::div//input")
    checkboxes_block_price_click = ss("//div[@class='filter-group__title' and contains (text(), 'Цена')]/following-sibling::div//span[@class='checkbox__text']")

    checkboxes_block_size_attrb = ss("//div[@class='filter-group__title' and contains (text(), 'Размер')]/following-sibling::div//input")
    checkboxes_block_size_click = ss("//div[@class='filter-group__title' and contains (text(), 'Размер')]/following-sibling::div//span[@class='checkbox__text']")


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

    @allure.step("Цикл запросов проверки Ботильоны ")
    def cycle_check_boots(self):

        product = 'boots'
        base_url = os.getenv('base_url') + 'api/section/filters/' + product
        #base_url = os.getenv('base_url')[:8] + os.getenv('base_url')[21:] + 'api/filters/' + product
        response_type_filter = requests.get(base_url).json()
        type_filter = list(response_type_filter.keys())

        #
        # for i in range(len(response_type_filter['colors'])):
        #     filter_color_id = str(response_type_filter['colors'][i]['id'])
        #     filter_color_name = str(response_type_filter['colors'][i]['name'])
        #
        #     url_color = os.getenv('base_url') + 'api/section/apply/' + product + '?' + type_filter[0][:-1] + '=' + filter_color_id
        #     #url_color = os.getenv('base_url')[:8] + os.getenv('base_url')[21:] + 'api/section/apply/' + product + '?' + type_filter[0][:-1] + '=' + filter_color_id
        #     request_color = requests.get(url_color).json()
        #
        #     checkbox_text = self.get_element_text(self.elements_block_color[i], " чекбокс выбора цвета").lower()
        #
        #     check_product_in_filters = len(request_color['items'])
        #     if check_product_in_filters == 0:
        #         continue
        #
        #     self.click(self.elements_block_color[i], " чекбокс выбора цвета")
        #     time.sleep(3)
        #
        #
        #
        #     for i in range(len(request_color['items'][0]['cells'])):
        #
        #         filter_color_name_product = self.get_element_text(self.cards_product_color_string_filter[i], ' название товара').capitalize()
        #
        #         filter_color_json = request_color['items'][0]['cells'][i]['entity']['models'][0]['color']['name']
        #         time.sleep(2)
        #         filter_color_name_product_json = request_color['items'][0]['cells'][i]['entity']['name']
        #         time.sleep(2)
        #
        #         page = BasePage()
        #         page.assert_check_coincidence(checkbox_text, filter_color_json, ' цвет товара в фильтре не соответсвует цвету товара в запросе api')
        #         page.assert_check_expressions(filter_color_name_product_json, filter_color_name_product, ' имя товара по фильтру не соответсвует имени товара из json' + filter_color_name_product_json + filter_color_name_product)
        #
        #
        #     status_checkbox1 = self.get_attribute(self.checkboxes_block_color_attrib[i-1], 'value')
        #     if status_checkbox1 == "true":
        #         self.click(self.checkboxes_block_color_click[i - 1], ' сброс состояния чекбокса')
        #
        #     time.sleep(2)
        #
        #
        # for i in range(len(response_type_filter['prices'])):
        #     filter_price_name = str(response_type_filter['prices'][i]['name'])
        #     filter_price_from = str(response_type_filter['prices'][i]['from'])
        #     filter_price_to = str(response_type_filter['prices'][i]['to'])
        #
        #     url = os.getenv('base_url') + 'api/section/apply/' + product + '?' + type_filter[1][:-1] + '[]' + '=' + filter_price_from + ',' + filter_price_to
        #     request_price = requests.get(url).json()
        #
        #     checkbox_text = self.get_element_text(self.checkboxes_block_price_click[i], " чекбокс выбора цвета").lower()
        #     checkbox_price_from = checkbox_text.partition("-")[0]
        #     if checkbox_price_from == "ДО":
        #         checkbox_price_from = "0"
        #     checkbox_price_to= checkbox_text.partition("-")[2]
        #
        #     self.click(self.checkboxes_block_price_click[i], " чекбокс выбора фильтра цены")
        #
        #     check_product_in_filters = len(request_price['items'])
        #
              # if check_product_in_filters == 0:
              #       continue
        #
        #     time.sleep(2)
        #
        #
        #
        #     for i in range(len(request_price['items'][0]['cells'])):
        #         filter_price_name_product = self.get_element_text(self.cards_product_color_string_filter[i], ' название товара').capitalize()
        #
        #         filter_price_json = request_price['items'][0]['cells'][i]['entity']['models'][0]['skus'][0]['price']
        #         time.sleep(2)
        #         filter_price_name_product_json = request_price['items'][0]['cells'][i]['entity']['name']
        #         time.sleep(2)
        #
        #         page = BasePage()
        #
        #         page.assert_check_range(int(checkbox_price_from), int(checkbox_price_to), filter_price_json, ' цвет товара в фильтре не соответсвует цвету товара в запросе api')
        #         page.assert_check_expressions(filter_price_name_product_json, filter_price_name_product, ' имя товара по фильтру не соответсвует имени товара из json')
        #
        #
        #
        #
        #     status_checkbox_price = self.get_attribute(self.checkboxes_block_price_attrb[i], 'value')
        #     if status_checkbox_price  == "true":
        #         self.click(self.checkboxes_block_price_click[i], ' сброс состояния чекбокса')
        #
        #     status_checkbox_price1 = self.get_attribute(self.checkboxes_block_price_attrb[i - 1], 'value')
        #     if status_checkbox_price1  == "true":
        #         self.click(self.checkboxes_block_price_click[i-1], ' сброс состояния чекбокса')
        #     status_checkbox_price2 = self.get_attribute(self.checkboxes_block_price_attrb[i - 2], 'value')
        #     if status_checkbox_price2  == "true":
        #         self.click(self.checkboxes_block_price_click[i-2], ' сброс состояния чекбокса')
        #     status_checkbox_price3 = self.get_attribute(self.checkboxes_block_price_attrb[i - 3], 'value')
        #     if status_checkbox_price3  == "true":
        #         self.click(self.checkboxes_block_price_click[i-3], ' сброс состояния чекбокса')

        for i in range(len(response_type_filter['sizes'])):
            filter_size_id = str(response_type_filter['sizes'][i]['id'])
            filter_size_name = str(response_type_filter['sizes'][i]['value'])


            url = os.getenv('base_url') + 'api/section/apply/' + product + '?' + type_filter[3][:-1] + '=' + filter_size_id
            request_size = requests.get(url).json()

            checkbox_text = self.get_element_text(self.checkboxes_block_size_click[i], " чекбокс выбора цвета").lower()


            self.click(self.checkboxes_block_size_click[i], " чекбокс выбора фильтра цены")

            check_product_in_filters = len(request_size['items'])

            if check_product_in_filters == 0:
                continue

            time.sleep(2)



            for i in range(len(request_size['items'][0]['cells'])):
                filter_size_name_product = self.get_element_text(self.cards_product_color_string_filter[i], ' название товара').capitalize()

                filter_size_json = request_size['items'][0]['cells'][i]['entity']['models'][0]['skus'][0]['size']['value']
                time.sleep(2)
                filter_size_name_product_json = request_size['items'][0]['cells'][i]['entity']['name']
                time.sleep(2)

                page = BasePage()

                page.assert_check_expressions(checkbox_text, filter_size_json, ' размер товара в фильтре не соответсвует размеру товара в запросе api')
                page.assert_check_expressions(filter_size_name_product_json, filter_size_name_product, ' имя товара по фильтру не соответсвует имени товара из json')




            status_checkbox_size = self.get_attribute(self.checkboxes_block_size_attrb[i], 'value')
            if status_checkbox_size == "true":
                self.click(self.checkboxes_block_size_click[i], ' сброс состояния чекбокса')

            status_checkbox_size1 = self.get_attribute(self.checkboxes_block_size_attrb[i - 1], 'value')
            if status_checkbox_size1 == "true":
                self.click(self.checkboxes_block_size_click[i-1], ' сброс состояния чекбокса')

            status_checkbox_size2 = self.get_attribute(self.checkboxes_block_size_attrb[i - 2], 'value')
            if status_checkbox_size2 == "true":
                self.click(self.checkboxes_block_size_click[i-2], ' сброс состояния чекбокса')

            status_checkbox_size3 = self.get_attribute(self.checkboxes_block_size_attrb[i - 3], 'value')
            if status_checkbox_size3 == "true":
                self.click(self.checkboxes_block_size_click[i-3], ' сброс состояния чекбокса')

            status_checkbox_size3 = self.get_attribute(self.checkboxes_block_size_attrb[i - 4], 'value')
            if status_checkbox_size3 == "true":
                self.click(self.checkboxes_block_size_click[i - 3], ' сброс состояния чекбокса')


    @allure.step("Цикл запросов проверки Лоферы")
    def cycle_check_loafers(self):
        base_url = os.getenv('base_url')[:8] + os.getenv('base_url')[21:] + 'api/section/filters/loafers'
        response_type_filter = requests.get(base_url).json()
        type_filter = list(response_type_filter.keys())

        for i in range(len(response_type_filter['colors'])):
            filter_color_id = str(response_type_filter['colors'][i]['id'])
            filter_color_name = str(response_type_filter['colors'][i]['name'])

            url_color = os.getenv('base_url')[:8] + os.getenv('base_url')[21:] + 'api/section/apply/loafers' + '?' + \
                        type_filter[0][:-1] + '=' + filter_color_id
            request_color = requests.get(url_color).json()

            status_checkbox = self.get_attribute(self.checkbox_block_color_attrib, 'value')
            if status_checkbox == "true":
                self.click(self.elements_block_color[i - 1], ' сброс состояния чекбокса')
            # elif status_checkbox == "":
            #     self.click(self.elements_block_color[i - 1], ' сброс состояния чекбокса')
            time.sleep(2)

            self.click(self.elements_block_color[i], " чекбокс выбора цвета")
            time.sleep(3)

            for i in range(len(request_color['items'][0]['cells'])):
                filter_color_name_product = self.get_element_text(self.cards_product_color_string_filter[i],
                                                                  ' название товара').capitalize()

                filter_color_json = request_color['items'][0]['cells'][i]['entity']['models'][0]['color']['name']
                time.sleep(2)
                filter_color_name_product_json = request_color['items'][0]['cells'][i]['entity']['name']
                time.sleep(2)

                page = BasePage()
                page.assert_check_coincidence(filter_color_name, filter_color_json,
                                              ' цвет товара в фильтре не соответсвует цвету товара в запросе api')
                page.assert_check_expressions(filter_color_name_product_json, filter_color_name_product,
                                              ' имя товара не соответствует цвету' + filter_color_name_product_json + filter_color_name_product)

                page = FilterPage()







