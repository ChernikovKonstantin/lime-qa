import json
import os
import time
from this import s

import allure
import pytest
import requests
from pages.account import AccountPage
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.filters import FilterPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.payment import PaymentPage


@allure.feature("Тесты фильтров")
@pytest.mark.usefixtures("setup")
class TestFilters:

    @allure.title("Тест цикла проверки цвета Лоферов")
    @allure.link("https://lmdev.testrail.io")
    def test_cycle(self):

        page = LoginPage()
        page.authorization()
        page.click(page.close_btn, "Закрыть профиль")
        time.sleep(2)

        page = CatalogPage()
        page.click(page.hamburger_menu, "гамбургер-меню")
        page.click(page.menu_link_shoes, "раздел Обувь")
        page.click(page.menu_subsection_shoes, "подраздел Лоферы")

        page = FilterPage()
        page.wait_element(page.button_filter_string)
        time.sleep(1)
        page.click(page.button_filter, ' кнопка фильтра')
        time.sleep(3)
        page.cycle()
    @allure.title("Тест фильтра по АПИ")
    @allure.link("https://lmdev.testrail.io")
    def test_api(self):

        #
        page = FilterPage()

        response_type_filter = page.type_filters()
        filter_color_black = str(response_type_filter['colors'][0]['id']) #черный
        #filter_color_beige = str(response_type_filter['colors'][1]['id'])



        # url_color_beige = os.getenv('base_url')[:8] + os.getenv('base_url')[21:] + 'api/section/apply/all_shoes' + '?color=' + filter_color_beige
        # response_filter_color_beige = requests.get(url_color_beige).json()
        # print(response_filter_color_beige)

        page = LoginPage()
        page.authorization()

        page = LoginPage()
        page.authorization()
        page.click(page.close_btn, "Закрыть профиль")
        time.sleep(2)

        page = CatalogPage()
        page.click(page.hamburger_menu, "гамбургер-меню")
        page.click(page.menu_link_shoes, "раздел Обувь")
        page.click(page.menu_subsection_shoes, "подраздел Лоферы")

        page = FilterPage()
        page.wait_element(page.button_filter_string)
        time.sleep(1)
        page.click(page.button_filter, ' кнопка фильтра')

        for i in range(len(self.elements_block_color)):
            self.click(self.elements_block_color[i], " чекбокс выбора цвета")
            color_filter = self.get_element_text(self.element_block_color, ' цвет чекбокса фильтра')

            url_color_black = os.getenv('base_url')[:8] + os.getenv('base_url')[21:] + 'api/section/apply/all_shoes' + '?color=' + filter_color_black
            response_filter_color_black = requests.get(url_color_black).json()

            for i in response_filter_color_black['items'][2]['cells'][2]['entity']['models'][0]['color']['name']:

                self.assert_check_expressions (color_filter, response_filter_color_black, ' цвета товаров в ответе API не соответсвует цвету чекбокса фильтра')



        # filters_color = response_type_filter['colors'][0]
        # for id_filters, name_filters in filters_color.items():
        #     print(id_filters, name_filters)


        # page.wait_element(page.button_filter_string)
        # time.sleep(1)
        # page.click(page.button_filter, ' кнопка фильтра')
        # time.sleep(3)
        # for i in range(len(self.elements_block_color)):
        #
        #     self.click(self.elements_block_color[i], " чекбокс выбора цвета")
        #     color_filter = self.get_element_text(self.element_block_color, ' цвет чекбокса фильтра')

        #response = page.rest_api()
        #json_dict = response['items'][2]['cells'][2]['entity']['models'][0]['color']['name']





        # #json_dict = response['items'][2]['cells'][2]['entity']['models'][0]['color']['name']
        # print(json_dict_type_filters)


        #print(type(json_dict))




