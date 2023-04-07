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


    @allure.title("Тест цикла проверки цвета Ботильоны")
    @allure.link("https://lmdev.testrail.io")
    def test_cycle(self):

        page = LoginPage()
        page.authorization()
        page.click(page.close_btn, "Закрыть профиль")
        time.sleep(2)

        page = CatalogPage()
        page.click(page.hamburger_menu, "гамбургер-меню")
        page.click(page.menu_link_shoes, "раздел Обувь")
        page.click(page.menu_subsection_shoes, "подраздел Ботильоны")

        page = FilterPage()
        page.wait_element(page.button_filter_string)
        time.sleep(1)
        page.click(page.button_filter, ' кнопка фильтра')
        time.sleep(3)
        page.cycle()

    @allure.title("Тест фильтра Ботильоны")
    @allure.link("https://lmdev.testrail.io")
    def test_api(self):
        page = CatalogPage()
        page.click(page.hamburger_menu, "гамбургер-меню")
        page.click(page.menu_section_shoes, "раздел Обувь")
        page.click(page.menu_subsection_shoes_botil, "подраздел Ботильоны>")

        page = FilterPage()
        time.sleep(1)
        page.click(page.button_filter, ' кнопка фильтра')

        page.cycle_check_boots()


    @allure.title("Тест фильтра Лоферы")
    @allure.link("https://lmdev.testrail.io")
    def test_api2(self):
        page = CatalogPage()
        page.click(page.hamburger_menu, "гамбургер-меню")
        page.click(page.menu_section_shoes, "раздел Обувь")
        page.click(page.menu_subsection_shoes_lofers, "подраздел Лоферы>")

        page = FilterPage()
        time.sleep(1)
        page.click(page.button_filter, ' кнопка фильтра')

        page.cycle_check_loafers()


        #page.cycle_check_color()


        # request_type_filter = page.type_filters()
        #
        # for i in range(len(request_type_filter)):
        #     type_filter = list(request_type_filter.keys())[i][:-1]
        #
        #
        #     for i in range(len(request_type_filter['colors'])):
        #         filter_color_id = str(request_type_filter['colors'][i]['id'])
        #         filter_color_name = str(request_type_filter['colors'][i]['name'])
        #
        #         url_color = os.getenv('base_url') + 'api/section/apply/loafers' + '?' + type_filter + '=' + filter_color_id
        #         request_color = requests.get(url_color).json()
        #
        #         status_checkbox = page.get_attribute(page.checkbox_block_color_attrib, 'value')
        #         if status_checkbox == "true":
        #             page.click(page.elements_block_color[i-1], ' сброс состояния чекбокса')
        #         page.click(page.elements_block_color[i], " чекбокс выбора цвета")
        #
        #         for i in range(len(request_color['items'][0]['cells'])):
        #
        #             filter_color_name_product = page.get_element_text(page.cards_product_color_string_filter[i], ' название товара').capitalize()
        #
        #             filter_color_json = request_color['items'][0]['cells'][i]['entity']['models'][0]['color']['name']
        #             filter_color_name_product_json = request_color['items'][0]['cells'][i]['entity']['name']
        #
        #             time.sleep(2)
        #             page = BasePage()
        #             page.assert_check_coincidence(filter_color_name, filter_color_json, ' цвет товара в фильтре не соответсвует цвету товара в запросе api' )
        #             page.assert_check_expressions(filter_color_name_product_json, filter_color_name_product, ' имя товара не соответствует цвету')
        #             page = FilterPage()







