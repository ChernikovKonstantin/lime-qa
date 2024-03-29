import json
import os
import time
from this import s
import re

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
from pages.smoke import SmokePage
from selene.support.shared import browser


@allure.feature("Смоук тест")
@pytest.mark.usefixtures("setup")
class TestSmoke:

    #ОСНОВНОЙ ЭКРАН


    # @allure.title("Основной экран / Переход с баннера к разделам каталога")
    # @allure.link("https://lmdev.testrail.io/index.php?/cases/view/849")
    # @pytest.mark.smoked
    # def test_main_screen_banners(self):
    #     page = SmokePage()
    #     page.cycle_banners()
    #     page.video()


    @allure.title("Основной экран / Лого LIME")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/852&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=121")
    @pytest.mark.smoked44
    def test_main_screen_logo(self):
        page = SmokePage()
        page.logo()

    @allure.title("Основной экран / Переход к экрану поиска")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/853")
    @pytest.mark.smoked
    def test_main_screen_main_menu_search(self):
        page = SmokePage()
        page.main_menu_search()


    @allure.title("Основной экран / Переход к экрану Избранное")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/854")
    @pytest.mark.smoked4
    def test_main_screen_main_menu_fav(self):
        page = SmokePage()
        page.click(page.button_favourites, " избранное")
        message_fav = page.get_element_text(page.string_message_favourites_01, " строка экрана избранное").replace("\n",
                                                                                                                   " ")
        page.assert_check_expressions("ВОЙДИТЕ ИЛИ ЗАРЕГИСТРИРУЙТЕСЬ, ЧТОБЫ ПРОСМОТРЕТЬ ВИШЛИСТ", message_fav,
                                      " ошибка сообщения на экране избранного")
        page.click(page.button_close_favourites, " закрыть избранное")

    @allure.title("Основной экран / Переход к экрану Личный кабинет")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/856")
    @pytest.mark.smoked4
    def test_main_screen_main_menu_lk(self):
        page = SmokePage()
        page.click(page.button_lk, " личный кабинет")
        page.click(page.button_login, " войти")
        page.wait_element(page.button_login_screen_login_string)
        page.click(page.button_close_screen_login, " закрыть экран входа")
        time.sleep(2)
        page.click(page.button_lk, " личный кабинет")
        time.sleep(2)
        page.click(page.button_registration, " зарегистрироваться")
        page.wait_element_assure(page.button_registration_screen_registration)
        page.click(page.button_close_screen, " закрыть экран регистрации")

    @allure.title("Основной экран / Переход к экрану Корзина")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/857")
    @pytest.mark.smoked4
    def test_main_screen_main_menu_basket(self):
        page = SmokePage()
        page.click(page.button_cart, " кнопка корзины")
        message_cart = page.get_element_text(page.message_empty_cart, " текст сообщения 'В вашей корзине нет покупок'")
        page.assert_check_expressions(message_cart, "В ВАШЕЙ КОРЗИНЕ НЕТ ПОКУПОК",
                                      " ошибка сообщения 'В вашей корзине нет покупок'")
        page.click(page.button_back_in_shop_empty_cart, " кнопка в магазин")
        page = CatalogPage()
        page.basket_changes_products_1399()
        time.sleep(1)
        page = SmokePage()
        page.click(page.button_cart_2, " кнопка корзины")
        page.wait_element(page.button_order_string)

        # НЕТ ПРОВЕРКИ ЭЛЕМЕНТА ЛОКАЛИЗАЦИИ




    @allure.title("Основной экран / Переход к экрану Каталог")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/855")
    @pytest.mark.smoked(3)
    def test_main_screen_menu(self):
        page = SmokePage()
        #page.catalog_menu_link()
        page.catalog_menu_parents_link_clothes()
        page.catalog_menu_parents_link_lingerie()
        #page.catalog_menu_parents_link_accessories()
        # page.catalog_menu_parents_link_shoes()
        # page.catalog_menu_parents_link_special_offer()
        # page.catalog_menu_parents_link_campaigns()

    @allure.title("Главная страница бургер меню")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/1599")
    @pytest.mark.smoked4
    def test_burger_menu(self):
        page = SmokePage()
        page.click(page.hamburger_menu, " гамбургер меню")
        time.sleep(2)
        page.wait_element_assure(page.dark_screen)
        page.wait_element_assure(page.block_catalog)
        page.click(page.element_plus, " список Дополнительно")
        #НУЖНО ДОБАВИТЬТ ПУНКТЫ В МЕНЮ
        page.wait_element_assure(page.cart)
        page.wait_element_assure(page.help)
        page.wait_element_assure(page.cart_bonus)
        page.wait_element_assure(page.account_or_name_user)
        page.click(page.hamburger_menu_close, " закрыть гамбургер меню")

        page.user_login()
        page.click(page.button_close_screen, " закрыть экран входа\регистрации")

        page = CatalogPage()
        page.click(page.basket_btn, "Переход в корзину")
        page = CartPage()
        page.cart_delete()
        page.open_url(os.getenv('base_url'))
        page = CatalogPage()
        page.favoutites_clear()
        page.click(page.button_close_fav, " закрыть экран избранного")
        page.click(page.hamburger_menu, " гамбургер меню")
        time.sleep(2)

        page = SmokePage()
        page.wait_element_assure(page.block_catalog)
        page.click(page.element_plus, " список Дополнительно")
        time.sleep(2)
        page.wait_element_assure(page.cart)
        page.wait_element_assure(page.help)
        page.wait_element_assure(page.cart_bonus)
        page.wait_element_assure(page.account_or_name_user)
        name_menu = page.get_element_text(page.account_or_name_user, " получить имя пользователя").upper()
        page.click(page.hamburger_menu_close, " закрыть гамбургер меню")

        page = HomePage()
        page.click(page.account_btn, " элемент аккаунта в меню")
        time.sleep(2)
        name_acc = browser.driver.execute_script("return document.querySelector('input[placeholder=Имя]').value").upper()
        surname_acc = browser.driver.execute_script("return document.querySelector('input[placeholder=Фамилия]').value").upper()
        name_account = name_acc + " " + surname_acc

        page.assert_check_expressions(name_menu, name_account, " имя пользователя не совпадает с именем пользователя в бургер меню")

    @allure.title("Проверка выпадающего меню каталога Одежда. Раздел с вложенными подразделами")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/1600")
    @pytest.mark.smoked4
    def test_burger_menu_check_products_sections(self):
        page = SmokePage()
        page.click(page.hamburger_menu, " гамбургер меню")
        page.wait_element_assure(page.dark_screen)
        page.click(page.category_parents_clothes, " категория ОДЕЖДА")
        #page.click_random_cat()
        page.click(page.category_parents_clothes, " закрыть категория ОДЕЖДА")
        time.sleep(3)
        page.click(page.hamburger_menu_close, " закрыть гамбургер меню")
        time.sleep(2)
        page.user_login()
        page.click(page.button_close_screen, " закрыть экран входа\регистрации")
        time.sleep(2)
        page.click(page.hamburger_menu, " гамбургер меню")
        page.wait_element_assure(page.dark_screen)
        page.click(page.category_parents_clothes, " категория ОДЕЖДА")
        time.sleep(2)
        page.click_random_cat()

        # КАТАЛОГ
    @allure.title("Экран 'Каталог' (Бургер-меню) / Подарочные карты")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/892")
    @pytest.mark.smoke4
    def test_burger_menu_bonus_card(self):
        page = SmokePage()
        page.click(page.hamburger_menu, " гамбургер меню")
        page.click(page.element_plus, " список Дополнительно")
        page.click(page.cart_bonus, " пункт Подарочная карта")
        time.sleep(1)
        url = page.get_url()
        page.assert_check_coincidence('gift', url, " не выполнен переход к экрану подарочной карты")


    @allure.title("Экран 'Коллекции' (Бургер-меню)/ Переход к карточке товара")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/893")
    @pytest.mark.smoke4
    def test_burger_menu_product_card(self):
        page = SmokePage()
        random_cat = page.click_random_cat_url()
        page.open_url(os.getenv('base_url') + random_cat)
        page.wait_element_assure(page.product_in_result_search)
        page.click_random_product()
        #time.sleep(3)
        page.wait_element_assure(page.title_product_in_cart)
        url = page.get_url()
        page.assert_check_coincidence('product', url, " не выполнен переход к карточке товара")

    @allure.title("Экран Каталог(Бургер-меню) / Раздел без подразделов")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/890&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=130")
    @pytest.mark.smoke4
    def test_burger_menu_check_products(self):
        page = CatalogPage()
        page.select_section_menu_new_collection()
        page = SmokePage()
        page.wait_element_hidden(page.block_catalog)
        time.sleep(1)
        url = page.get_url()
        page.assert_check_coincidence("catalog/new", url, " переход в каталог не выполнен")
        page.wait_element_assure(page.catalog_image)

    @allure.title("Просмотр карточки товара")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/894")
    @pytest.mark.smoked1(6)
    def test_cart_product(self):
        page = CatalogPage()
        page.select_section_menu_sales_all()
        page = SmokePage()
        time.sleep(3)
        page.wait_element_assure(page.img_in_catalog)
        page.click(page.img_in_catalog, " продукт в каталоге")
        time.sleep(3)
        page.wait_element_assure(page.title_product_in_cart)
        page.wait_element_assure(page.share_string_card_products)
        #page.wait_element_assure(page.imges_in_cart_slider)
        page.wait_element_assure(page.img_in_cart_slider)
        time.sleep(5)
        # Цикл проверки верикальных карточе товаров
        # for i in range(len(page.imges_in_cart_slider)):
        #     resolution = page.imges_in_cart_slider[i].size
        #     height = (resolution['height'])
        #     width = (resolution['width'])
        #     page.assert_check_comparison(height, width, " изображение не портретное")
        page = CatalogPage()
        page.wait_element_assure(page.add_to_cart)
        page.wait_element_assure(page.colors_selector)
        page.wait_element_assure(page.add_favorite_btn)
        page.wait_element_assure(page.button_drop_down_size)
        page.wait_element_assure(page.product_price_sale_text)

        page = SmokePage()
        page.user_login()
        page.click(page.button_close_screen, " закрыть экран входа\регистрации")
        page = CatalogPage()
        page.select_section_menu_sales_all()
        page = SmokePage()
        time.sleep(3)
        page.wait_element_assure(page.img_in_catalog)
        page.click(page.img_in_catalog, " продукт в каталоге")
        time.sleep(2)
        page.wait_element_assure(page.title_product_in_cart)
        page.wait_element_assure(page.share_string_card_products)
        page.wait_element_assure(page.imges_in_cart_slider)
        time.sleep(5)
        # for y in range(len(page.imges_in_cart_slider)):
        #     resolution = page.imges_in_cart_slider[y].size
        #     height = (resolution['height'])
        #     width = (resolution['width'])
        #     page.assert_check_comparison(height, width, " изображение не портретное")

        page = CatalogPage()
        page.wait_element_assure(page.add_to_cart)
        page.wait_element_assure(page.colors_selector)
        page.wait_element_assure(page.add_favorite_btn)
        page.wait_element_assure(page.button_drop_down_size)
        page.wait_element_assure(page.product_price_sale_text)

    # КОРЗИНА

    @allure.title("Проверка добавления товара в корзину (Неавторизованный пользователь)")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/898")
    @pytest.mark.smoked1(7)
    def test_cart_add_product_anonim(self):
        page = CatalogPage()
        page.basket_changes_products_1399()
        time.sleep(2)
        page = CatalogPage()
        page.click(page.add_to_cart, "добавить в корзину")

        page = SmokePage()
        title_product = page.get_element_text(page.title_product_in_cart, " название товара в карточке")
        value_counter_basket = page.check_counter_basket()
        page.assert_check_expressions("1", value_counter_basket, " некорректная работа счетчика корзины")
        page.click(page.button_cart_2, " переход в корзину")
        time.sleep(2)

        page = SmokePage()
        title_product_basket = page.get_element_text(page.title_product_in_basket, " название товара в корзине")
        page.assert_check_expressions(title_product_basket, title_product, " названиетовара в карточке не соответсвет названию товара в корзине")

    @allure.title("Проверка добавления товара в корзину (Авторизованный пользователь)")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/899")
    @pytest.mark.smoked2(1)
    def test_cart_add_product_user(self):

        page = SmokePage()
        page.user_login()
        page.click(page.button_close_screen, " закрыть экран входа\регистрации")

        page.open_url(os.getenv('base_url') + "/ru_ru/catalog/bodysuits")
        time.sleep(2)
        page = CatalogPage()
        page.click(page.choose_a_product_1399, "Товар с ценой 1999")
        time.sleep(2)
        page.click(page.add_to_cart, "добавить в корзину")

        page = SmokePage()
        title_product = page.get_element_text(page.title_product_in_cart, " название товара в карточке")
        value_counter_basket = page.check_counter_basket()
        page.assert_check_expressions("1", value_counter_basket, " некорректная работа счетчика корзины")
        page.click(page.button_cart_2, " переход в корзину")
        time.sleep(2)

        page = SmokePage()
        title_product_basket = page.get_element_text(page.title_product_in_basket, " название товара в корзине")
        page.assert_check_expressions(title_product_basket, title_product,
                                      " названиетовара в карточке не соответсвет названию товара в корзине")

    @allure.title("Проверка удаления товара из корзины (Авторизованный пользователь)")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/900")
    @pytest.mark.smoked2(2)

    def test_cart_del_product_user(self):
        page = SmokePage()
        page.user_login()
        page.click(page.button_close_screen, " закрыть экран входа\регистрации")
        page = CatalogPage()
        page.basket_add_many_products()
        time.sleep(2)
        page = SmokePage()
        value_counter_basket = page.check_counter_basket()

        page.click(page.button_cart_2, " переход в корзину")
        time.sleep(2)
        title_product_basket = page.get_element_text(page.title_product_in_basket, " название товара в корзине")
        page = CartPage()
        page.wait_element_assure(page.block_product)
        page.click(page.button_del, " удалить 1 товар в корзине")
        time.sleep(5)
        page = SmokePage()
        title_product_basket_after_del = page.get_element_text(page.title_product_in_basket, " название товара в корзине")
        page.assert_check_not_expressions(title_product_basket, title_product_basket_after_del, " товар не удален из корзины")
        page.open_url(os.getenv('base_url'))
        time.sleep(2)
        value_counter_basket_after_del = page.check_counter_basket()
        page.assert_check_expressions(int(value_counter_basket), (int(value_counter_basket_after_del) + 1), " счетчик не уменьшился после удаления товара из корзины")

    # @allure.title("Экран Корзина Товара нет в наличии")
    # @allure.link("https://lmdev.testrail.io/index.php?/cases/view/901")
    # def test_cart_add_product_not_available(self):
    #     page = SmokePage()
    #     page.user_login()
    #     page.click(page.button_close_screen, " закрыть экран входа\регистрации")
    #     PaymentPage.click(self.basket_btn, "Переход в корзину")
    #     CartPage.cart_delete()
    #     page = CatalogPage()
    #     page.basket_add_last_product()
    #     page = SmokePage()
    #     page.user_logout()
    #     page.user2_login()
    #     page.click(page.button_close_screen, " закрыть экран входа\регистрации")
    #     PaymentPage.click(self.basket_btn, "Переход в корзину")
    #     CartPage.cart_delete()
    #     page = CatalogPage()
    #     page.basket_add_last_product()
    #     page = SmokePage()
    #     page.user_logout()
    #     page.user_login()
    #     page.click(page.button_close_screen, " закрыть экран входа\регистрации")
    #     page = PaymentPage
    #     page.preview_payment_in_cart()
    #     page.pay_order()
    #     page = SmokePage()
    #     page.user_logout()
    #     page.user2_login()
    #     page.click(page.button_close_screen, " закрыть экран входа\регистрации")
    #     PaymentPage.click(self.basket_btn, "Переход в корзину")

    @allure.title("Экран Корзина / Товар со скидкой")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/902&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=131")
    @pytest.mark.smoked2(3)
    def test_cart_product_discount(self):
        page = CatalogPage()
        page.basket_add_discount_product()
        page = SmokePage()
        page.click(page.button_cart_2, " переход в корзину")
        page = PaymentPage()
        page.sum_order_in_basket_with_discount()


    # ПРОФИЛЬ


    # @allure.title("Профиль пользователя")
    # @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=122")
    # def test_profile(self):
    #
    #
    #
    #     page.user_registration_and_first_lk()
    #     page.user_profile_with_order()

    @allure.title("Профиль / экран вход/регистрация")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/858")
    @pytest.mark.smoked2(4)
    def test_login_screen(self):
        page = SmokePage()
        page.click(page.button_lk, " личный кабинет")
        page.login_screen()

    @allure.title("Профиль / экран войти(Негативный)")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/859")
    @pytest.mark.smoked2(5)
    def test_login_negative(self):
        page = SmokePage()
        page.user_login_not_valid()

    @allure.title("Профиль / экран войти")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/861")
    @pytest.mark.smoked2(6)
    def test_login(self):
        page = SmokePage()
        page.user_login()

    @allure.title("Профиль / регистрация (Негативный)")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/862")
    @pytest.mark.smoked2(7)
    def test_registration_negative(self):
        page = SmokePage()
        page.user_registration_not_valid()

    @allure.title("Профиль / регистрация")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/862")

    def test_registration(self):
        page = SmokePage()
        page.user_registration()

    @allure.title("Профиль / мои данные / первый вход в аккаунт")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/872")

    def test_first_login(self):
        page = SmokePage()
        page.user_first_lk()

    @allure.title("Профиль / мои данные /")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/880")
    @pytest.mark.smoke3
    def test_profile_order(self):
        page = PaymentPage()
        page.preview_payment()
        page.check_product_for_order()
        #page.check_del_old_card()

        page.field_valid_card()
        page.to_pay_btn.click()
        time.sleep(2)
        #page.success_btn.click()

        page = SmokePage()
        number_order = (re.sub('[^0-9]', "", page.get_element_text(page.message_number_order, ' сумма заказа после оформления')))

        page.click(page.button_lk, " личный кабинет")

        page.wait_element(page.message_registration_screen_string)
        page.wait_element(page.button_change_password_string)
        page.wait_element(page.button_save_changes_string)
        #page.wait_element(page.message_mailing_string)
        page.wait_element(page.button_delete_accaunt_string)
        page.wait_element(page.button_logout_account_string)
        page.wait_element(page.message_orders_string)
        time.sleep(10)
        page.wait_element(page.orders_string)

        number_ord = (re.sub('[^0-9]', "",
                             page.get_element_text(page.message_number_order_lk, ' сумма заказа в личном кабинете')))

        number_order_lk = number_ord[:-12]

        page.assert_check_expressions(number_order, number_order_lk, " оформленный заказ отсутсвует в личном кабинете")



    @allure.title("Экран поиска")
    @allure.link("https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=123")
    @pytest.mark.smoke3
    def test_search(self):
        page = SmokePage()
        page.search_successful_text()
        page.open_url(os.getenv('base_url'))
        page.search_successful_article()
        page.search_not_result()

    @allure.title("Оплата карта + валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/903")
    @pytest.mark.smoke3
    def test_payment_cart_valid_promo(self):
        page = PaymentPage()
        page.preview_payment()
        page.set_text(page.promo_code_field, "XHGFAH", "Промо код")
        page.sum_order_with_discount()
        #page.check_del_old_card()
        page.field_valid_card()
        page.pay_order()

    @allure.title("Оплата карта + валидный промокод, несколько товаров")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/904")

    def test_payment_cart_valid_promo_many_prducts(self):
        page = PaymentPage()
        page.preview_payment_many_products()
        page.set_text(page.promo_code_field, "XHGFAH", "Промо код")
        page.sum_order_with_discount_many()
        #page.check_del_old_card_2_products()
        page.field_valid_card()
        page.pay_order()

    @allure.title("Оплата карта + не валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/905")

    def test_payment_cart_no_valid_promo(self):

        page = PaymentPage()
        page.preview_payment()
        page.set_text(page.promo_code_field, "00000", "Промо код")
        page.check_del_old_card()
        #page.field_valid_card()
        page.check_payment_promo_not_valid()

    @allure.title("Проверка скидки при безналичной оплате на сайте заказа суммой > 6000")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/906&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=124")
    @pytest.mark.smoke2
    def test_payment_cart_order_more_6000(self):
        page = PaymentPage()
        page.preview_payment_6000()
        page.sum_order_with_discount()
        page.change_value_products_in_payment_1_unit()
        page.check_without_discount()
        page.change_value_products_in_payment_5_unit()
        page.sum_order_with_discount()
        page.check_del_old_card()
        page.field_valid_card()
        page.pay_order()

    @allure.title("Проверка применения промокодов для заказов 6000 < Σ < 6000")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/907")
    @pytest.mark.smoke2
    def test_payment_promocodes_6000_sum_6000(self):
        page = PaymentPage()
        page.preview_payment_6000()
        page.enter_valid_promo_0()
        page.sum_order_with_discount()
        page.enter_valid_promo_10()
        page.sum_order_with_discount()
        page.enter_valid_promo_25()
        page.sum_order_with_discount()
        page.change_value_products_in_payment_1_unit()
        page.enter_valid_promo_0()
        page.check_without_discount()

    # @allure.title("Оплата картой ошибка оплаты")
    # @allure.link("https://lmdev.testrail.io/index.php?/cases/view/908")
    # @pytest.mark.smoke2
    # def test_payment_card_error(self):
    #     page = PaymentPage()
    #     page.preview_payment()
    #     page.click(page.type_of_delivery_courier, "Выбор типа доставки Курьер")
    #     page.click(page.type_of_payment_card, "Выбор типа оплаты Карта")
    #     #page.check_del_old_card()
    #     page.field_valid_card()
    #     page.pay_order_error()

    @allure.title("Оплата при получении, доставка курьером")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/912")
    @pytest.mark.smoke2
    def test_pay_receiving_courier(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_courier, 'Выбор типа доставки Доставка курьером')
        page.click(page.type_of_payment_receiving, 'Выбор типа оплаты При получении')
        page.wait_element_not_visible(page.string_data_card)
        page.pay_order_post_payment()

    @allure.title("Оплата банковской картой самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/913")
    @pytest.mark.smoke2
    def test_card_self(self):
        page = PaymentPage()
        page.preview_payment_old_card()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.field_self_and_pic_point()
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')
        page.check_del_old_card()
        page.field_valid_card()
        page.pay_order()

    @allure.title("Оплата банковской картой (недостаточно средств), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/914")
    @pytest.mark.smoke2
    def test_card_self_no_many(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.field_self_and_pic_point()
        time.sleep(1)

        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')
        page.check_del_old_card()
        page.field_valid_card()
        page.set_text(page.card_number_field, "2203 0000 0000 0043", " тестовый номер карты  с ошибкой Недостаточно средств")
        page.pay_order_without_check()

        page.wait_element_assure(page.error_card_not_money_string)

    @allure.title("Оплата банковской картой(не существующая карта), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/915")
    @pytest.mark.smoke2
    def test_card_self_no_valid_card(self):
        page = PaymentPage()
        page.preview_payment()

        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.field_self_and_pic_point()
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')
        page.check_del_old_card()
        page.field_valid_card()
        page.set_text(page.card_number_field, "4012 8888 8888 1882",
                      " не валидный номер карты")
        #page.pay_order_without_check()
        page.wait_element(page.error_card_not_not_valid_card)
        page.wait_element_assure(page.to_pay_btn)
        page.click( page.to_pay_btn, "кнопка оплаты")

        page.wait_element_not_visible(page.success_btn_string)
        page.wait_element(page.error_card_not_not_valid_card)

    @allure.title("Оплата банковской картой, ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/920")
    @pytest.mark.smoke2
    def test_pay_card_pick_point(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page.check_del_old_card()
        page.field_valid_card()
        page.pay_order()

    @allure.title("Оплата банковской картой(недостаточно средств), ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/921")
    @pytest.mark.smoke2
    def test_pay_card_no_many_pick_point(self):
        page = PaymentPage()
        page.preview_payment()

        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page.check_del_old_card()
        page.field_valid_card()
        page.set_text(page.card_number_field, "2203 0000 0000 0043",
                      " тестовый номер карты с ошибкой недостаточно средств")
        page.pay_order_without_check()
        page.wait_element_assure(page.error_card_not_money_string)

    @allure.title("Оплата банковской картой(не существующая карта), ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/922")
    @pytest.mark.smoke2
    def test_pay_card_not_valid_pick_point(self):
        page = PaymentPage()
        page.preview_payment()

        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page.check_del_old_card()
        page.field_valid_card()
        page.set_text(page.card_number_field, "4012 8888 8888 1882",
                      " не валидный номер карты")
        # page.pay_order_without_check()
        page.wait_element(page.error_card_not_not_valid_card)
        page.wait_element_assure(page.to_pay_btn)
        page.click(page.to_pay_btn, "кнопка оплаты")

        page.wait_element_not_visible(page.success_btn_string)
        page.wait_element(page.error_card_not_not_valid_card)

    @allure.title("Оплата подарочной картой, доставка курьером+ добавить новый адрес ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/909")
    @pytest.mark.smoke2
    def test_bonus_card_courier(self):
        page = PaymentPage()
        page.preview_payment()
        page = SmokePage()
        page.add_address_courier()
        page.payment_bonus_card()
        page = PaymentPage()
        page.pay_order_without_3d()

    @allure.title("Оплата подарочной картой(не достаточно средств), доставка курьером")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/910")
    @pytest.mark.smoke2
    def test_bonus_card_no_many(self):
        page = PaymentPage()
        page.preview_payment_many_products()
        page = SmokePage()
        #page.add_address_courier()
        page.payment_bonus_card_no_many()
        page = PaymentPage()
        page.wait_element_assure(page.error_bonus_card_not_money)
        page.click(page.to_pay_btn, "кнопка оплаты")
        page.wait_element_assure(page.error_bonus_card_not_money)


    @allure.title("Оплата подарочной картой(НЕ ВАЛИДНАЯ КАРТА), доставка курьером ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/911")
    @pytest.mark.smoke2
    def test_pay_bonus_card_not_valid(self):
        page = PaymentPage()
        page.preview_payment()
        page = SmokePage()
        page.payment_bonus_card_not_valid()
        page = PaymentPage()
        page.wait_element_assure(page.error_bonus_card_not_valid)
        page.click(page.to_pay_btn, "кнопка оплаты")
        page.wait_element_assure(page.error_bonus_card_not_valid)

    @allure.title("Оплата подарочной картой(не существующая карта), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/916")
    @pytest.mark.smoke2
    def test_pay_bonus_card_not_valid_self(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.field_self_and_pic_point()

        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')

        page = SmokePage()
        page.payment_bonus_card_not_valid()
        page = PaymentPage()
        page.wait_element_assure(page.error_bonus_card_not_valid)
        page.click(page.to_pay_btn, "кнопка оплаты")
        page.wait_element_assure(page.error_bonus_card_not_valid)

    @allure.title("Оплата подарочной картой(недостаточно средств), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/917")
    @pytest.mark.smoke2
    def test_pay_bonus_card_no_many_self(self):
        page = PaymentPage()
        page.preview_payment_many_products()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.field_self_and_pic_point()
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин')

        page = SmokePage()
        page.payment_bonus_card_no_many()
        page = PaymentPage()
        page.wait_element_assure(page.error_bonus_card_not_money)
        page.click(page.to_pay_btn, "кнопка оплаты")
        page.wait_element_assure(page.error_bonus_card_not_money)

    @allure.title("Оплата подарочной картой, самовывоз ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/918")
    @pytest.mark.smoke2
    def test_bonus_card_self(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.field_self_and_pic_point()
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин')
        page = SmokePage()
        page.payment_bonus_card()
        page = PaymentPage()
        page.pay_order_without_3d()

    @allure.title("Оплата банковской картой + подарочная карта+ промкод ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/919")
    @pytest.mark.smoke2
    def test_card_bonus_card_self_promo(self):
        page = PaymentPage()
        page.preview_payment_many_products()
        page = SmokePage()
        page.payment_bonus_card_promocode()
        page = PaymentPage()
        #page.field_valid_card()
        page.wait_element_assure(page.error_bonus_card_not_money2)
        page.click(page.button_dop_pay, " дополнительная оплата")


        page = SmokePage()
        page.payment_bonus_card_promocode()
        page = PaymentPage()
        page.enter_valid_promo_10()
        price_without_discount = (int(re.sub('[^0-9]', "", page.get_element_text(page.price_without_discount_bonus_card,
                                                                                 'Получение суммы заказа без промо'))))
        page.assert_check_expressions("0", price_without_discount, " сумма заказа в строке Итого перессчитывается некорректно")


        page = PaymentPage()
        page.pay_order_without_3d()

    @allure.title("Оплата подарочной картой, ПВЗ ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/923")
    @pytest.mark.smoke2
    def test_bonus_card_pick_point(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page = SmokePage()
        page.payment_bonus_card()
        page = PaymentPage()
        page.pay_order_without_3d()

    @allure.title("Оплата подарочной картой(не существующая карта), ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/924")
    @pytest.mark.smoke2
    def test_pay_bonus_card_not_valid_pick_point(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')

        page = SmokePage()
        page.payment_bonus_card_not_valid()
        page = PaymentPage()
        page.wait_element_assure(page.error_bonus_card_not_valid)
        page.click(page.to_pay_btn, "кнопка оплаты")
        page.wait_element_assure(page.error_bonus_card_not_valid)

    @allure.title("Оплата подарочной картой(недостаточно средств), ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/925")
    @pytest.mark.smoke2
    def test_pay_bonus_card_no_many_pick_point(self):
        page = PaymentPage()
        page.preview_payment_many_products()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')

        page = SmokePage()
        page.payment_bonus_card_no_many()
        page = PaymentPage()
        page.wait_element_assure(page.error_bonus_card_not_money)
        page.click(page.to_pay_btn, "кнопка оплаты")
        page.wait_element_assure(page.error_bonus_card_not_money)

    @allure.title("Оплата банковской картой + подарочная карта+ промкод + ПВЗ ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/926&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=124")
    @pytest.mark.smoke2
    def test_card_bonus_card_self_promo(self):
        page = PaymentPage()
        page.preview_payment_many_products()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page = SmokePage()
        page.payment_bonus_card_promocode()
        page = PaymentPage()
        # page.field_valid_card()
        page.wait_element_assure(page.error_bonus_card_not_money2)
        page.click(page.button_dop_pay, " дополнительная оплата")
        # page.field_valid_card()

        page = SmokePage()
        page.payment_bonus_card_promocode()
        page = PaymentPage()
        price_without_discount = (int(re.sub('[^0-9]', "", page.get_element_text(page.price_without_discount_bonus_card,
                                                                                 'Получение суммы заказа без промо'))))
        price_discount = round((price_without_discount * 0.1), -2)

        page.enter_valid_promo_10()
        page.field_valid_card()
        price_with_discount = (int(re.sub('[^0-9]', "", page.get_element_text(page.price_with_discount_bonus_card,'Получение суммы заказа без промо'))))

        page.assert_check_expressions(price_with_discount, (price_without_discount-price_discount),
                                      " сумма заказа в строке Итого перессчитывается некорректно")

        page = PaymentPage()
        page.pay_order_without_3d()

    @allure.title("Проверка добавление товара в избранное из каталога (Неавторизованный пользователь)")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/885&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=125")
    @pytest.mark.smoke2
    def test_add_fav_anonim(self):

        page = CatalogPage()
        page.select_section_menu_sales_all()
        time.sleep(1)
        page = SmokePage()
        page.add_favourites_catalog()
        value_fav = page.check_element_fav_menu()

        page = BasePage()
        page.assert_check_expressions("1", value_fav, " не верное количество товаров в иконке избранное")


    @allure.title("Проверка добавления и удаления  товара из Избранного (Авторизованный пользователь)")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/886")
    @pytest.mark.smoke2
    def test_add_del_fav_user(self):

        page = SmokePage()
        page.user_login()
        page.click(page.button_close_screen_login, " закрыть экран профиля")

        page = CatalogPage()
        page.favoutites_clear()

        page.open_url(os.getenv('base_url') + "/ru_ru/catalog/sale")
        page = SmokePage()
        page.add_favourites_catalog()
        time.sleep(1)

        page.open_url(os.getenv('base_url') + "/ru_ru/catalog/new")
        page = SmokePage()
        page.add_favourites_catalog()
        time.sleep(1)

        value_fav = page.check_element_fav_menu()
        page = BasePage()
        page.assert_check_expressions("2", value_fav, " не верное количество товаров в иконке избранное")

        page = SmokePage()
        page.del_favourites_cart_product()
        time.sleep(3)
        value_fav = page.check_element_fav_menu()
        page.check_del_product_fav_screen()
        page = BasePage()
        page.assert_check_expressions("1", value_fav, " не верное количество товаров в иконке избранное")
        page = SmokePage()
        page.del_favourites_cart_product()

    @allure.title("Избранное / перейти в карточку товара")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/888")
    @pytest.mark.smoke2
    def test_fav_card_product_check(self):
        page = SmokePage()
        page.user_login()
        page.click(page.button_close_screen_login, " закрыть экран профиля")

        page = CatalogPage()
        page.favoutites_clear()
        page.open_url(os.getenv('base_url') + "/ru_ru/catalog/all_shoes")
        page = SmokePage()
        page.add_favourites_cart()
        page.check_add_fav()

    # @allure.title("Проверка добавления и удаления  товара из Избранного (Авторизованный пользователь)")
    # @allure.link("https://lmdev.testrail.io/index.php?/cases/view/887")
    #
    # def test_add_del_fav_user(self):
    #     page = SmokePage()
    #     page.user_login()
    #     page.click(page.button_close_screen_login, " закрыть экран профиля")
    #
    #     page = CatalogPage()
    #     page.favoutites_clear()
    #     page.select_section_menu_shoes_all()
    #     page = SmokePage()
    #     page.add_favourites_catalog()
    #
    #     value_fav = page.check_element_fav_menu()
    #     page = BasePage()
    #     page.assert_check_expressions("1", value_fav, " не верное количество товаров в иконке избранное")
    #
    #     page = CatalogPage()
    #     page.select_section_menu_shoes_all()
    #     page = SmokePage()
    #     page.del_favourites_catalog()
    #
    #
    #     page = SmokePage()
    #     value_fav = page.check_element_fav_empty_menu()
    #     page.assert_check_expressions("", value_fav, " избранное не пустое")
    #
    #     page = SmokePage()
    #     page.check_full_screen_fav()































































