import os
import time
import re

import allure
from selene.api import be, have, s
from selene.support.shared.jquery_style import ss

from pages.account import AccountPage
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.home import HomePage
from pages.login import LoginPage
from selene.api import browser

from pages.payment import PaymentPage


class SmokePage(BasePage):

    # locators main page
    banners_main_image = ss("//div[@class = 'slide' and @style != 'cursor: pointer;']")
    video_main_image = s("//video")
    block_icon_string = "//div[@class='App isHomepage page-index isAppNotify isEmptyCart']"
    first_catalog_image = s("(//picture/img)[1]")
    first_catalog_video = s("(//video[@class='d-none d-md-block'])[1]")
    first_catalog_video_attribute = s("(//video[@class='d-none d-md-block'])[1]//child::*")
    #interesnaia_construkciya = s(//span[contains(@class,"mainmenu__link has-children")])
    all_bunners = ss("//div[@class='slide']")
    logo_string = "(//div[@class='logo'])[2]"

    # button main menu

    button_search = s("//button[@class='SearchBox__button']")
    input_search = s("//input[@type = 'text']")
    input_search_active = s("//input[@type = 'text' and @class='SearchBox__input active']")
    input_search_active_full =s("//input[@type = 'text' and @class='SearchBox__input fill active']")
    input_search_active_string = "//input[@type = 'text' and @class='SearchBox__input active']"
    product_in_result_search = s("//div[@class = 'CatalogProduct__title']")
    product_in_result_search_string = "//div[@class = 'CatalogProduct__title']"
    products_in_result_search = ss("//div[@class = 'CatalogProduct__title']/a")
    product_article = s("//div[@class='product__article']")
    message_search_not_result = s("//div[contains(text(), 'По вашему запросу ничего не найдено')]")

    button_favourites = s("(//div[@class='SvgIcon'])[2]")
    string_message_favourites_01 = s("//div[@class='headline-4']")
    button_close_favourites = s('//div[@class = "SvgIcon IButtonIcon"]')

    button_lk = s("(//div[@class='SvgIcon'])[1]")
    button_login = s("//button[@class='btn btn-block btn-outline btn-primary']")
    button_login_string = "//button[@class='btn btn-block btn-outline btn-primary']"
    button_login_screen_login_string = "//button[@class='btn btn-block']"
    button_close_screen_login = s("//div[@class='SvgIcon IButtonIcon']")

    button_registration = s("//button[@class='btn btn-block btn-primary']")
    button_registration_string = "//button[@class='btn btn-block btn-primary']"
    button_registration_screen_registration_string = "//button[@class='btn btn-block']"
    button_close_screen = s("//div[@class='SvgIcon IButtonIcon']")

    button_cart = s("(//div[@class='SvgIcon'])[4]")
    message_empty_cart = s("//div[@class='ViewCart__Empty__Message']/p")
    button_back_in_shop_empty_cart = s("//button[@class='btn ViewCart__Empty__Message__Button']")
    button_order_string = "//button[@class = 'btn btn-block']"



    # locators burger and catalog

    hamburger_menu = s("(//div[@class='hamburger-menu burger'])[2]")
    hamburger_menu_string = "(//div[@class='hamburger-menu burger'])[2]"
    categoryes_link = ss("//li[@class='mainmenu__item']/a")
    category_parents_clothes = s("(//li[@class='mainmenu__item']/span)[1]")
    category_parents_lingerie = s("(//li[@class='mainmenu__item']/span)[2]")
    category_parents_accessories = s("(//li[@class='mainmenu__item']/span)[3]")
    category_parents_shoes = s("(//li[@class='mainmenu__item']/span)[4]")
    category_parents_special_offer = s("(//li[@class='mainmenu__item']/span)[5]")
    category_parents_campaigns = s("(//li[@class='mainmenu__item']/span)[6]")
    categoryes_sub = ss("//li[@class='mainmenu__item']/ul/li/a")
    categoryes_sub_sub = ss("//ul[@class='mainmenu-children mainmenu__children']/li/ul/li/a")

    #locators login screen

    h1_srting = "//h1[contains(text(), 'Личный кабинет')]"
    link_help_string = "//a[@href = '/help' and contains(text(), 'Руководство по покупке')]"
    link_contacts_string = "//a[@href = '/contacts' and contains(text(), 'Контакты')]"
    link_about_string = "//a[@href = '/about' and contains(text(), 'Компания')]"
    link_shops_string = "//a[@href = '/shops' and contains(text(), 'Магазины')]"

    # locators registration screen

    message_registration_screen_string = "//div[contains(text(), 'Личные данные')]"
    button_change_password_string = "//button[contains(text(), 'Изменить пароль')]"
    button_save_changes_string = "//button[contains(text(), 'Сохранить изменения')]"
    message_mailing_string = "//span[contains(text(), 'Я хочу получать новостную рассылку')]"
    button_delete_accaunt_string ="//a[contains(text(), 'Удалить аккаунт')]"
    button_logout_account_string = "//button[contains(text(), 'Выйти')]"
    orders_string = "//div[@class = 'PreviewOrders__item']"
    message_orders_string = "//strong[contains(text(), 'Мои заказы')]"
    message_number_order = s("//div[@class = 'OrderComplete__note']/div")
    message_number_order_lk = s("//div[@class = 'PreviewOrders']/following-sibling::div")




    # ОСНОВНОЙ ЭКРАН

    @allure.step('Цикл проверки баннеров')
    def cycle_banners(self):

        for i in range(len(self.banners_main_image)):
            list_first_attribute_banners = ['https://cache-limeshop.cdnvideo.ru/limeshop/aa/734083954af8f1a65bf3a11ed9d9900155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/73344231819676f30b73f11ed9d9600155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/73164154295cc9644a39611ed9d8f00155d011401.jpeg?q=85&w=440',
                                            'https://cache-limeshop.cdnvideo.ru/limeshop/aa/73107092616306c58bff011ec9d3700155d011401.jpeg?q=85&w=440',
                                            '']
            url_main = self.get_url()
            self.click(self.banners_main_image[i], " баннер")
            first_image = self.get_attribute(self.first_catalog_image, "data-src")
            self.assert_check_expressions(list_first_attribute_banners[i], first_image, " некорректное отображение порядка товаров в каталоге")
            self.browser_back()
            url_main_return = self.get_url()
            self.wait_element(self.block_icon_string) #ожидание блока иконок белого цвета
            self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")

    @allure.step('Проверка видео')
    def video(self):

        video = 'https://cache-limeshop.cdnvideo.ru/limeshop/landing-pages/summer-basic-23/01_desc+ipad.mp4'
        url_main = self.get_url()
        self.click(self.video_main_image, " видео")
        first_video = self.get_attribute(self.first_catalog_video_attribute, "src")
        self.assert_check_expressions(video, first_video,
                                      " некорректное отображение видео в каталоге")
        first_video_loop = self.get_attribute(self.first_catalog_video, "loop")
        self.assert_check_expressions("true", first_video_loop,
                                      " нет тега автовоспроизведения видео")
        self.browser_back()
        url_main_return = self.get_url()
        self.wait_element(self.block_icon_string)  # ожидание блока иконок белого цвета
        self.assert_check_expressions(url_main, url_main_return, " ошибка адреса при возврате на главную страницу")

    @allure.step('Проверка логотипа')
    def logo(self):
        for i in range(len(self.all_bunners)):
            self.move_to(browser.driver.find_element_by_xpath("(//div[@class='slide'])["+(str(i+1))+"]"))
            #self.move_to(self.all_bunners[i])
            self.wait_element(self.logo_string)

    @allure.step('Поиск в главном меню')
    def main_menu_search(self):
        self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active)
        self.set_text(self.input_search_active, '6498-375', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        self.wait_element_assure(self.product_in_result_search)

        for i in range(len(self.products_in_result_search)):
            self.click(self.products_in_result_search[i], " продукт в результатах поиска")
            self.wait_element_assure(self.product_in_result_search)
            article_text = self.get_element_text(self.product_article, " артикул товара")
            article = article_text.partition(" ")[2]
            self.assert_check_expressions(article, "6498-375", " значение артикула не соответствует")
            self.browser_back()
            self.wait_element_assure(self.product_in_result_search)

        self.field_clear(self.input_search_active_full, " инпут поиска")
        self.set_text(self.input_search_active_full, 'ожерелье', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        time.sleep(3)
        self.wait_element_assure(self.product_in_result_search)
        for y in range(len(self.products_in_result_search)):
            product_text = self.get_element_text(self.products_in_result_search[y], " название товара Ожерелье").lower()
            print(product_text)
            self.assert_check_coincidence("ожерел", product_text, " некорреткный вывод результатов поиска")

    @allure.step('Переходы по разделам главного меню')
    def main_menu(self):

        self.click(self.button_favourites, " избранное")
        message_fav = self.get_element_text(self.string_message_favourites_01, " строка экрана избранное").replace("\n", " ")
        self.assert_check_expressions("ВОЙДИТЕ ИЛИ ЗАРЕГИСТРИРУЙТЕСЬ, ЧТОБЫ ПРОСМОТРЕТЬ ВИШЛИСТ", message_fav, " ошибка сообщения на экране избранного")
        self.click(self.button_close_favourites, " закрыть избранное")

        self.click(self.button_lk, " личный кабинет")
        self.click(self.button_login, " войти")
        self.wait_element(self.button_login_screen_login_string)
        self.click(self.button_close_screen_login, " закрыть экран входа")

        self.click(self.button_lk, " личный кабинет")
        self.click(self.button_registration, " зарегистрироваться")
        self.wait_element(self.button_registration_screen_registration_string)
        self.click(self.button_close_screen, " закрыть экран регистрации")

        self.click(self.button_cart, " кнопка корзины")
        message_cart = self.get_element_text(self.message_empty_cart, " текст сообщения 'В вашей корзине нет покупок'")
        self.assert_check_expressions(message_cart, "В ВАШЕЙ КОРЗИНЕ НЕТ ПОКУПОК", " ошибка сообщения 'В вашей корзине нет покупок'")
        self.click(self.button_back_in_shop_empty_cart, " кнопка в магазин")
        page = CatalogPage()
        page.basket_changes_products_1399()
        self.click(self.button_cart, " кнопка корзины")
        self.wait_element(self.button_order_string)

        # НЕТ ПРОВЕРКИ ЭЛЕМЕНТА ЛОКАЛИЗАЦИИ

    @allure.step('Разделы меню каталога (ссылки)')
    def catalog_menu_link(self):
        self.click(self.hamburger_menu, " гамбургер меню")
        for i in range(len(self.categoryes_link)):
           #self.wait_element(self.hamburger_menu_string)
            self.click(self.categoryes_link[i], " раздел меню")
            time.sleep(1)
            url_catalog = self.get_url()
            self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
            self.browser_back()
            self.click(self.hamburger_menu, " гамбургер меню")

    @allure.step('Разделы меню ОДЕЖДА (выпадающие меню)')
    def catalog_menu_parents_link_clothes(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_clothes, " категория ОДЕЖДА")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории ОДЕЖДА ")
            time.sleep(1)
            url_catalog = self.get_url()
            if  url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_clothes, " категория ОДЕЖДА")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_clothes, " категория ОДЕЖДА")
                    self.click(self.categoryes_sub[i], " подраздел категории ОДЕЖДА ")

    @allure.step('Разделы меню НИЖНЕЕ БЕЛЬЕ (выпадающие меню)')
    def catalog_menu_parents_link_lingerie(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории НИЖНЕЕ БЕЛЬЕ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_lingerie, " категория НИЖНЕЕ БЕЛЬЕ")
                    self.click(self.categoryes_sub[i], " подраздел категории НИЖНЕЕ БЕЛЬЕ ")

    @allure.step('Разделы меню АКСЕССУАРЫ (выпадающие меню)')
    def catalog_menu_parents_link_accessories(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории АКСЕССУАРЫ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_accessories, " категория АКСЕССУАРЫ")
                    self.click(self.categoryes_sub[i], " подраздел категории АКСЕССУАРЫ")

    @allure.step('Разделы меню ОБУВЬ (выпадающие меню)')
    def catalog_menu_parents_link_shoes(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_shoes, " категория ОБУВЬ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории ОБУВЬ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_shoes, " категория ОБУВЬ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_shoes, " категория ОБУВЬ")
                    self.click(self.categoryes_sub[i], " подраздел категории ОБУВЬ")

    @allure.step('Разделы меню СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ (выпадающие меню)')
    def catalog_menu_parents_link_special_offer(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("catalog", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_special_offer, " категория СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
                    self.click(self.categoryes_sub[i], " подраздел категории СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")

    @allure.step('Разделы меню КОМПАНИИ (выпадающие меню)')
    def catalog_menu_parents_link_campaigns(self):
        self.open_url(os.getenv('base_url'))
        self.click(self.hamburger_menu, " гамбургер меню")
        self.click(self.category_parents_campaigns, " категория КОМПАНИИ")

        for i in range(len(self.categoryes_sub)):

            url_main = self.get_url()

            self.click(self.categoryes_sub[i], " подраздел категории КОМПАНИИ")
            time.sleep(1)
            url_catalog = self.get_url()
            if url_catalog != url_main:
                self.assert_check_coincidence("summer", url_catalog, " переход выполнен не в каталог")
                self.browser_back()
                self.click(self.hamburger_menu, " гамбургер меню")
                self.click(self.category_parents_campaigns, " категория КОМПАНИИ")

            elif url_catalog == url_main:
                for y in range(len(self.categoryes_sub_sub)):
                    self.click(self.categoryes_sub_sub[y], " подраздел подраздела")
                    time.sleep(1)
                    url_catalog = self.get_url()
                    self.assert_check_coincidence("summer", url_catalog, " переход выполнен не в каталог")
                    self.browser_back()
                    self.click(self.hamburger_menu, " гамбургер меню")
                    self.click(self.category_parents_campaigns, " категория КОМПАНИИ")
                    self.click(self.categoryes_sub[i], " подраздел категории КОМПАНИИ")

    # ПРОФИЛЬ

    @allure.step('Профиль экран входа')
    def login_screen(self):

        self.wait_element(self.h1_srting)
        self.wait_element(self.link_help_string)
        self.wait_element(self.link_contacts_string)
        self.wait_element(self.link_about_string)
        self.wait_element(self.link_shops_string)
        self.wait_element(self.button_login_string)
        self.wait_element(self.button_registration_string)
        self.click(self.button_close_screen, " закрыть экран входа\регистрации")

    @allure.step('Логин с невалидным паролем')
    def user_login_not_valid(self):

        page = HomePage()
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()
        time.sleep(3)

        page = LoginPage()
        page.login(email="chernikov.kv@lime-shop.com", password=("VTer38XXXXXX"))
        page.check_login_error()

    @allure.step('Успешный логин')
    def user_login(self):
        page = HomePage()
        page.click_account_btn()
        page = AccountPage()
        page.click_enter_btn()
        page = LoginPage()
        page.login(email=os.getenv("test_user"), password=os.getenv("password"))
        page.check_logout_btn_is_visible()

    @allure.step('Регистрация с не валидными данными')
    def user_registration_not_valid(self):
        page = HomePage()


        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields_smoke()

        list_errors = page.get_text_error_smoke()

        assert list_errors[0] == ('некорректный e-mail'), print('Некорректный текст ошибки регистрации')
        assert list_errors[1] == ('некорректный номер телефона'), print('Некорректный текст ошибки регистрации')
        assert list_errors[2] == ('введенные пароли не совпадают'), print('Некорректный текст ошибки регистрации')

    @allure.step('Регистрация с валидными данными + Первый вход в профиль')
    def user_registration_and_first_lk(self):
        page = HomePage()

        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields()
        page = LoginPage()
        page.check_logout_btn_is_visible()

        self.wait_element(self.message_registration_screen_string)
        self.wait_element(self.button_change_password_string)
        self.wait_element(self.button_save_changes_string)
        self.wait_element(self.message_mailing_string)
        self.wait_element(self.button_delete_accaunt_string)
        self.wait_element(self.button_logout_account_string)

    @allure.step('Мои данные (профиль с покупками)')
    def user_profile_with_order(self):

        page = PaymentPage()
        page.preview_payment()
        page.check_product_for_order()
        page.to_pay_btn.click()
        time.sleep(2)
        page.success_btn.click()


        #number_order = self.get_element_text(self.message_number_order, " стрка с номером заказа")
        number_order = (re.sub('[^0-9]', "", self.get_element_text(self.message_number_order, ' сумма заказа после оформления')))


        self.click(self.button_lk, " личный кабинет")

        self.wait_element(self.message_registration_screen_string)
        self.wait_element(self.button_change_password_string)
        self.wait_element(self.button_save_changes_string)
        self.wait_element(self.message_mailing_string)
        self.wait_element(self.button_delete_accaunt_string)
        self.wait_element(self.button_logout_account_string)
        self.wait_element(self.message_orders_string)
        time.sleep(5)
        self.wait_element(self.orders_string)


        number_ord = (re.sub('[^0-9]', "", self.get_element_text(self.message_number_order_lk, ' сумма заказа в личном кабинете')))
        number_order_lk = number_ord[:-12]

        self.assert_check_expressions(number_order, number_order_lk, " оформленный заказ отсутсвует в личном кабинете")

    @allure.step('Поиск по тексту')
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/881")
    def search_successful_text(self):
        self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active)
        self.set_text(self.input_search_active, 'ожерелье', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        time.sleep(3)
        self.wait_element_assure(self.product_in_result_search)
        for i in range(len(self.products_in_result_search)):
            product_text = self.get_element_text(self.products_in_result_search[i], " название товара Ожерелье").lower()
            print(product_text)
            self.assert_check_coincidence("ожерел", product_text, " некорреткный вывод результатов поиска")

    @allure.step('Поиск по артикулу')
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/882")
    def search_successful_article(self):
        #self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active_full)
        self.set_text(self.input_search_active_full, '6498-375', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        self.wait_element_assure(self.product_in_result_search)

        for i in range(len(self.products_in_result_search)):
            self.click(self.products_in_result_search[i], " продукт в результатах поиска")
            self.wait_element_assure(self.product_in_result_search)
            article_text = self.get_element_text(self.product_article, " артикул товара")
            article = article_text.partition(" ")[2]
            self.assert_check_expressions(article, "6498-375", " значение артикула не соответствует")
            self.browser_back()
            self.wait_element_assure(self.product_in_result_search)

    @allure.step('Поиск без результата')
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/883")
    def search_not_result(self):
        #self.click(self.button_search, " поиск")
        self.wait_element_assure(self.input_search_active_full)
        self.set_text(self.input_search_active_full, 'фуфайка', " инпут поиска")
        self.push_enter(self.input_search_active_full, " инпут поиска")
        self.wait_element_assure(self.message_search_not_result)

    @allure.step('Оплата. Карта + валидный промокод')
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/903")
    def test_product_registration_cart_promo_code(self):

        page = PaymentPage()
        page.preview_payment()
        #page.enter_valid_promo()
        page.cycle_type_promo_code()
        title_thank_you_page = page.pay_order()

        assert title_thank_you_page == "СПАСИБО!", print("Ошибка сообщения. Текст ошибки: " + title_thank_you_page)




























































