import os
import time
from this import s

import allure
import pytest

from pages.account import AccountPage
from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.payment import PaymentPage


@allure.feature("Тесты оплаты")
@pytest.mark.usefixtures("setup")
class TestPayment:




    @allure.title("Оплата картой + валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/441")
    @pytest.mark.order
    def test_product_registration_cart_promo_code(self):
        page = LoginPage()
        page.authorization()
        time.sleep(1)
        page.click_close_btn()
        time.sleep(3)

        page = CatalogPage()
        page.click(page.basket_btn, "Переход в корзину")
        time.sleep(1)
        page = CartPage()
        page.cart_delete()
        time.sleep(1)
        page.open_url(os.getenv('base_url'))

        page = CatalogPage()
        page.basket_changes_products_1399()
        page.basket_btn.click()
        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(5)

        page = PaymentPage()
        page.check_product_for_order()
        title_thank_you_page = page.payment_promo_valid()
        print(title_thank_you_page)

        assert title_thank_you_page == "СПАСИБО!", print("Ошибка сообщения. Текст ошибки: " + title_thank_you_page)

    @allure.title("Оплата картой + валидный промокод, несколько товаров в корзине")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/445")
    @pytest.mark.order
    def test_product_registration_cart_promo_code_many_products(self):
        page = LoginPage()
        page.authorization()
        page.click_close_btn()
        time.sleep(2)

        page = CatalogPage()
        page.click(page.basket_btn, "Переход в корзину")
        time.sleep(1)
        page = CartPage()
        page.cart_delete()
        page.open_url(os.getenv('base_url'))

        page = CatalogPage()
        page.basket_multiple_products()
        page.basket_btn.click()
        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(2)
        page = PaymentPage()
        page.check_product_for_order()
        title_thank_you_page = page.payment_promo_valid_many_products()
        print(title_thank_you_page)

        assert title_thank_you_page == "СПАСИБО!", print("Ошибка сообщения. Текст ошибки: " + title_thank_you_page)


    @allure.title("Оплата картой +  не валидный промокод")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/443")
    @pytest.mark.order
    def test_product_registration_cart_not_valid_promo_code(self):
        page = LoginPage()
        page.authorization()
        page.click_close_btn()
        time.sleep(2)

        page = CatalogPage()
        page.click(page.basket_btn, "Переход в корзину")
        time.sleep(1)
        page = CartPage()
        page.cart_delete()
        page.open_url(os.getenv('base_url'))

        page = CatalogPage()
        page.basket_changes_products()
        time.sleep(1)
        page.basket_btn.click()

        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(2)
        page = PaymentPage()
        page.check_product_for_order()
        page.payment_promo_not_valid()


    @allure.title("Оплата картой заказа суммой более 6000 с формированием заказа в корзине")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/442&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=80")
    @pytest.mark.order
    def test_product_discount_cart_6000(self):
        page = LoginPage()
        page.authorization()
        page.click_close_btn()
        time.sleep(2)

        page = CatalogPage()
        page.click(page.basket_btn, "Переход в корзину")
        time.sleep(1)
        page = CartPage()
        page.cart_delete()
        page.open_url(os.getenv('base_url'))

        page = CatalogPage()
        page.basket_changes_products_1399()
        page.basket_btn.click()
        time.sleep(1)

        page = PaymentPage()
        page.check_product_for_order()

        page = CartPage()
        page.change_value_products_in_cart()
        time.sleep(2)
        page.wait_element(page.making_an_order_btn_string)
        page.click_making_an_order_btn()
        time.sleep(1)

        page = PaymentPage()
        page.sum_order_with_discount_6000()
        page.change_value_products_in_payment_1_unit()
        page.check_wait_message_without_discount()
        page.change_value_products_in_payment_5_unit()
        page.sum_order_with_discount_6000()

        page.filling_fields_registration_product()

        self.to_pay_btn.click()
        time.sleep(2)
        self.success_btn.click()
        time.sleep(2)
        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, '')
        assert title_thank_you_page == "СПАСИБО!", print("Ошибка сообщения. Текст ошибки: " + title_thank_you_page)

    @allure.title("Проверка применения скидок для заказа > 6000")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/444")
    @pytest.mark.order
    def test_discount(self):

        page = LoginPage()
        page.authorization()
        page.click_close_btn()
        time.sleep(2)

        page = CatalogPage()
        page.click(page.basket_btn, "Переход в корзину")
        time.sleep(1)
        page = CartPage()
        page.cart_delete()
        time.sleep(1)
        page.open_url(os.getenv('base_url'))

        time.sleep(1)
        page = CatalogPage()
        page.basket_changes_products_1399()
        page.basket_btn.click()
        time.sleep(1)

        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        time.sleep(1)
        page.change_value_products_in_cart()
        time.sleep(1)
        page.click_making_an_order_btn()
        time.sleep(1)

        page = PaymentPage()
        page.check_product_for_order()
        page.cycle_type_promo_code()

    @allure.title("Оплата картой, ошибка оплаты")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/451")
    @pytest.mark.order
    def test_check_payment_card_error(self):
        page = PaymentPage()
        page.preview_payment()

        page.click(page.type_of_delivery_courier, "Выбор типа доставки Курьер")
        page.click(page.type_of_payment_card, "Выбор типа оплаты Карта")

        page.wait_element(page.to_pay_btn_string)
        page.click(page.to_pay_btn, "Нажать кнопку Оплатить заказ")

        page.wait_element(page.success_btn_fault_string)
        page.click(page.success_btn_fault, "Нажать кнопку Неудача на странице тестовой оплаты")
        time.sleep(5)

        page.wait_element(page.error_card_payment_string)
        error = page.get_element_text(page.error_card_payment, 'Получить текст ошибки оплаты на странице оформления заказа')
        error_text = "ОПЛАТА НЕ ПРОШЛА: Свяжитесь с вашим банком или воспользуйтесь другой картой"
        page.assert_check_expressions(error,error_text,'Не отображается ошибка некорректной оплаты')


    @allure.title("Оплата подарочной картой, доставка курьером+ добавить новый адрес")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/452")

    @allure.title("Оплата подарочной картой(не достаточно средств), доставка курьером")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/466")

    @allure.title("Оплата подарочной картой(НЕ ВАЛИДНАЯ КАРТА), доставка курьером")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/453")


    @allure.title("Оплата при получении, доставка курьером")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/454")
    @pytest.mark.order
    def test_pay_receiving_courier(self):

        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_courier, 'Выбор типа доставки Доставка курьером')
        page.click(page.type_of_payment_receiving, 'Выбор типа оплаты При получении')
        page.wait_element_not_visible(page.string_data_card)

        page.click(page.to_pay_btn, 'Клик кнопку Оплатить')
        title_thank_you_page = page.get_element_text(page.title_thank_you_page_text, 'Сообщение об успешной покупке')
        page.assert_check_expressions(title_thank_you_page, "СПАСИБО!", 'Ошибка! Оплата не выполнена.')

    @allure.title("Оплата банковской картой, самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/455")
    @pytest.mark.order
    def test_pay_card_self(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')

        page.click(page.to_pay_btn, 'Клик кнопку Оплатить')
        page.wait_element(page.success_btn_string)
        page.click(page.success_btn, 'кнопка Успешно')
        title_thank_you_page = page.get_element_text(page.title_thank_you_page_text, 'Получить текст сообщения об успешной покупке')
        page.assert_check_expressions(title_thank_you_page, "СПАСИБО!", 'Ошибка! Оплата не выполнена.')

    @allure.title("Оплата банковской картой(недостаточно средств), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/456")
    @pytest.mark.order
    def test_pay_card_self_not_money(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')
        page.set_text(page.card_number_field, "4012 8888 8888 1881", " тестовый номер карты  с ошибкой Недостаточно средств")
        page.click(page.to_pay_btn, 'Клик кнопку Оплатить')
        page.wait_element(page.success_btn_string)
        page.click(page.success_btn, 'кнопка Успешно')

        page.wait_element(page.error_card_not_money_string)

    @allure.title("Оплата банковской картой(не существующая карта), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/457")
    @pytest.mark.order
    def test_pay_card_not_valid_sel(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_self, 'Выбор типа доставки Самовывоз')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор пункта самовывоза')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот магазин"')
        page.set_text(page.card_number_field, "4012 8888 8888 1882", " Не валидный номер карты")
        page.click(page.to_pay_btn, 'Клик кнопку Оплатить')

        page.wait_element_not_visible(page.success_btn_string)
        page.wait_element(page.error_card_not_not_valid_card)


    @allure.title("Оплата подарочной картой(не существующая карта), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/458")

    @allure.title("Оплата подарочной картой(недостаточно средств), самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/465")

    @allure.title("Оплата подарочной картой, самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/460")

    @allure.title("Оплата банковской картой + подарочная карта+ промкод, самовывоз")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/459")

    @allure.title("Оплата банковской картой, ПВЗ ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/461")
    @pytest.mark.order
    def test_pay_card_pick_point(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page.click(page.to_pay_btn, 'Клик кнопку Оплатить')

        page.wait_element(page.success_btn_string)
        page.click(page.success_btn, 'кнопка Успешно')
        title_thank_you_page = page.get_element_text(page.title_thank_you_page_text, 'Получить текст сообщения об успешной покупке')
        page.assert_check_expressions(title_thank_you_page, "СПАСИБО!", 'Ошибка! Оплата не выполнена.')

    @allure.title("Оплата банковской картой(недостаточно средств), ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/462")
    @pytest.mark.order
    def test_pay_card_pick_point_not_money(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page.set_text(page.card_number_field, "4012 8888 8888 1881", " тестовый номер карты  с ошибкой Недостаточно средств")
        page.click(page.to_pay_btn, 'Клик кнопку Оплатить')
        page.wait_element(page.success_btn_string)
        page.click(page.success_btn, 'кнопка Успешно')

        page.wait_element(page.error_card_not_money_string)

    @allure.title("Оплата банковской картой(не существующая карта), ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/463&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=90")
    @pytest.mark.order
    def test_pay_card_not_valid_pick_point(self):
        page = PaymentPage()
        page.preview_payment()
        page.click(page.type_of_delivery_pic_point, 'Выбор типа доставки Пункт выдачи товара')
        page.click(page.point_self_and_pic_point_delivery, 'Выбор ПВЗ')
        page.click(page.button_choise_point, 'Кнопка "Выбрать этот ПВЗ"')
        page.set_text(page.card_number_field, "4012 8888 8888 1882", " Не валидный номер карты")
        page.click(page.to_pay_btn, 'Клик кнопку Оплатить')

        page.wait_element_not_visible(page.success_btn_string)
        page.wait_element(page.error_card_not_not_valid_card)

    @allure.title("Оплата подарочной картой, ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/464")

    @allure.title("Оплата подарочной картой(не существующая карта), ПВЗ ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/467")

    @allure.title("Оплата подарочной картой(недостаточно средств), ПВЗ ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/468")

    @allure.title("Оплата банковской картой + подарочная карта+ промкод, ПВЗ")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/469")
    def zaglushka(self):
        print('zaglishka')

























