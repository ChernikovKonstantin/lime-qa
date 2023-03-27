import os
import time
import re

import allure
from selene.api import be, have, s

from pages.base import BasePage
from pages.cart import CartPage
from pages.catalog import CatalogPage
from pages.login import LoginPage


class PaymentPage(BasePage):
    # locators

    card_number_field = s("//input[@type='text' and @placeholder='Введите номер карты']")
    validity_period_field = s("//input[@type='text' and @placeholder='Дата окончания срока действия']")
    card_holder_field = s("//input[@type='text' and @placeholder='Владелец карты']")
    security_code_field = s("//input[@type='text' and @placeholder='Код безопасности CVV2']")
    promo_code_field = s("//input[@type='text' and @placeholder='Промокод']")
    to_pay_btn = s("//button[@class ='btn btn-block']")
    to_pay_btn_string = "//button[@class ='btn btn-block']"
    success_btn = s("//button[@class = 'button button_primary']")
    success_btn_fault = s("//button[@class='button button_secondary']")
    success_btn_fault_string = "//button[@class='button button_secondary']"

    title_thank_you_page_text = s("//div[contains(text(),'Спасибо!')]")
    dropdown_quantity_product_on_payment = s("//div[@class='DropdownList__container DropdownList__inline']")
    # dropdown_quantity_product = s("(//div[@class='SvgIcon'])[2]/child::*")
    dropdown_quantity_product_select_5_on_payment = s("(//span[@class='DropdownList__title'])[5]")
    dropdown_quantity_product_select_1_on_payment = s("(//span[@class='DropdownList__title'])[1]")
    error_card_payment = s('// div[contains(text(), "ОПЛАТА НЕ ПРОШЛА: Свяжитесь с вашим банком или воспользуйтесь другой картой")]')



    #locators_delivery

    type_of_delivery_courier = s("//span[contains(text(), 'Доставка курьером')]")
    type_of_delivery_self = s("//span[contains(text(), 'Самовывоз из магазина')]")
    type_of_delivery_pic_point = s("//span[contains(text(), 'Пункты выдачи')]")
    point_self_and_pic_point_delivery = s("//div[@class='PickPointSelector__item']")

    # locators_type_payment
    type_of_payment_card = s("//span[contains(text(), 'Оплата картой онлайн')]")
    type_of_payment_gift_card = s("//span[contains(text(), 'Подарочной картой')]")
    type_of_payment_receiving = s("//span[contains(text(), 'При получении')]")





    # locators for promocode

    price_finally_block_cart_text = s("//span[@class='sale']") # цена с промо в блоке корзина
    price_finally_block_cart_text_string = "//span[@class='sale']"
    icon_discount_percent_block_cart_text = s('//span[@class="percent"]') # иконка процента промо
    icon_discount_percent_block_cart_text_string = '//span[@class="percent"]'
    discount_string = '//div[contains(text(), " Скидка на заказ")]'# строка Скидка на заказ
    price_discount_text = s('(//div[@class="CustomerCartSummary__value"])[3]/span')# сумма скидки
    price_without_discount_text = s('(//div[@class="CustomerCartSummary__value"])[2]/span')# итоговая сумма без промокода
    price_finally_text = s('(//div[@class="CustomerCartSummary__value"])[5]/span')# Итого
    promo_code_error_string = "//div[contains(text(), 'промокод не найден')]"  #ошибка промокода






    @allure.step('Заполнение полей при оформлении товара')
    def filling_fields_registration_product(self):
        time.sleep(2)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.to_pay_btn.click()
        self.success_btn.click()
        # title_thank_you_page = self.get_element_text(self.title_cart_text, 'Заголовок в корзине')

    @allure.step('Проверка при оплате картой + валидный промо')
    def payment_promo_valid(self):
        time.sleep(3)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.set_text(self.promo_code_field, "XHGFAH", "Промо код")

        # Проверка суммы корзины с промо

        price_finally_block_cart, price_without_discount, price_discount, \
            price_finally, icon_discount_percent_block_cart, price_discount_icon = self.sum_order_with_promo()

        assert price_without_discount == price_finally + price_discount, \
            print('Ошибка проверки: цена с промо  + сумма скидки = итого')

        assert price_without_discount == price_finally_block_cart + price_discount, \
            print('Ошибка проверки: цена с промо в блоке корзина + сумма скидки = итого')

        assert price_finally_block_cart == price_without_discount - price_discount_icon, \
            print('Ошибка проверки: цена с промо в блоке корзина =  итого х %промо')
        #(round((int(price_without_discount[:-5])), -1))

        time.sleep(2)
        self.to_pay_btn.click()
        time.sleep(2)
        self.success_btn.click()
        time.sleep(2)
        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, '')

        return title_thank_you_page

    def sum_order_with_promo(self):

        self.wait_element(self.discount_string)
        price_finally_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_block_cart_text, 'Получение итоговой суммы заказа из блока Корзина'))))
        #price_without_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Цена без промо')))), -1)
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промокода'))))
        price_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text, 'Сумма скидки по промокоду, с округлением в большую сторону')))), -1)
        price_finally = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text, 'Получение итоговой суммы заказа'))))
        icon_discount_percent_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.icon_discount_percent_block_cart_text, 'Получение процента скидки'))))
        price_discount_icon = round(price_without_discount*(icon_discount_percent_block_cart/100), -1)

        return price_finally_block_cart, price_without_discount, price_discount, price_finally, icon_discount_percent_block_cart, price_discount_icon

    @allure.step('Проверка при оплате картой + валидный промо_несколько товаров в корзине')
    def payment_promo_valid_many_products(self):
        time.sleep(3)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.set_text(self.promo_code_field, "XHGFAH", "Промо код")

        # Проверка суммы корзины с промо

        price_finally_block_cart, price_without_discount, price_discount, \
            price_finally, icon_discount_percent_block_cart, price_discount_icon = self.sum_order_with_promo()

        assert price_without_discount == price_finally + price_discount, \
            print('Ошибка проверки: цена с промо  + сумма скидки = итого')

        assert price_finally == price_without_discount - price_discount_icon, \
            print('Ошибка проверки: цена с промо в блоке корзина =  итого х %промо')
        # (round((int(price_without_discount[:-5])), -1))

        time.sleep(2)
        self.to_pay_btn.click()
        time.sleep(2)
        self.success_btn.click()
        time.sleep(2)
        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, '')

        return title_thank_you_page

    @allure.step('Проверка при оплате картой + не валидный промо')
    def payment_promo_not_valid(self):
        time.sleep(3)
        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")
        self.set_text(self.promo_code_field, "000000", "Не валидный Промокод")

        self.wait_element(self.promo_code_error_string)
        self.wait_element_not_visible(self.discount_string)
        self.wait_element_not_visible(self.price_finally_block_cart_text_string)
        self.wait_element_not_visible(self.icon_discount_percent_block_cart_text_string)

        self.wait_element(self.to_pay_btn_string)
        self.to_pay_btn.click()
        self.wait_element(self.promo_code_error_string)

    @allure.step('Проверка суммы заказа с учетом скидки 6000')
    def sum_order_with_discount_6000(self):
        self.wait_element(self.discount_string)
        self.wait_element(self.icon_discount_percent_block_cart_text_string)
        price_finally_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_block_cart_text, 'Получение итоговой суммы заказа из блока Корзина'))))
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промокода'))))
        price_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text, 'Сумма скидки по промокоду, с округлением в большую сторону')))),-1)
        price_finally = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text, 'Получение итоговой суммы заказа'))))
        icon_discount_percent_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.icon_discount_percent_block_cart_text, 'Получение процента скидки'))))
        price_discount_icon = round(price_without_discount * (icon_discount_percent_block_cart / 100), -1)

        #return price_finally_block_cart, price_without_discount, price_discount, price_finally, icon_discount_percent_block_cart, price_discount_icon

        assert price_without_discount == price_finally + price_discount, print('Ошибка проверки: цена с промо  + сумма скидки = итого')

        assert price_without_discount == price_finally_block_cart + price_discount, print('Ошибка проверки: цена с промо в блоке корзина + сумма скидки = итого')

        assert price_finally_block_cart == price_without_discount - price_discount_icon, print('Ошибка проверки: цена с промо в блоке корзина =  итого х %промо')

        print(price_without_discount)
        print(price_finally_block_cart)
        print(price_discount)
        print(price_discount_icon)

    @allure.step("Изменение количества товара на 1 единицу на экране оформления заказа")
    def change_value_products_in_payment_1_unit(self):
        self.dropdown_quantity_product_on_payment.click()
        time.sleep(1)
        self.dropdown_quantity_product_select_1_on_payment.click()

    @allure.step("Изменение количества товара на 5 единиц на экране оформления заказа")
    def change_value_products_in_payment_5_unit(self):
        self.dropdown_quantity_product_on_payment.click()
        time.sleep(1)
        self.dropdown_quantity_product_select_5_on_payment.click()

    @allure.step('Проверка полей скидок при оплате картой + не валидный промо')
    def check_payment_promo_not_valid(self):
        self.wait_element(self.promo_code_error_string)
        self.wait_element_not_visible(self.discount_string)
        self.wait_element_not_visible(self.price_finally_block_cart_text_string)
        self.wait_element_not_visible(self.icon_discount_percent_block_cart_text_string)

        self.wait_element(self.to_pay_btn_string)
        self.to_pay_btn.click()
        self.wait_element(self.promo_code_error_string)

    @allure.step('Проверка отсутсвия элементов скидки')
    def check_wait_message_without_discount(self):
        self.wait_element_not_visible(self.discount_string)
        self.wait_element_not_visible(self.price_finally_block_cart_text_string)
        self.wait_element_not_visible(self.icon_discount_percent_block_cart_text_string)

    @allure.step('Цикл проверки промокодов')
    def cycle_type_promo_code(self):

        list_promo = ['LIMEPR', 'XHGFAH', 'SOTRUDN25']

        for i in range(len(list_promo)):

            self.set_text(self.promo_code_field, list_promo[i], "Установка промокода в поле")

            time.sleep(2)

            percent_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.icon_discount_percent_block_cart_text, 'Извлечение процента из элемента процент скидки'))))

            price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промо'))))

            price_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text, 'Получение суммы скидки'))))

            if percent_discount == 5:

                self.assert_check_expressions(price_discount, (round((price_without_discount * 0.05), -1)),'Проверка скидки 5%')
                #assert price_discount == round((price_without_discount * 0.05), -1)

            elif percent_discount == 10:
                self.assert_check_expressions(price_discount, (round((price_without_discount * 0.1), -1)),'Проверка скидки 10%')
                #assert price_discount == round((price_without_discount * 0.1), -1)

            elif percent_discount == 25:
                self.assert_check_expressions(price_discount, (round((price_without_discount * 0.25), -1)),'Проверка скидки 25%')
                #assert price_discount == round((price_without_discount * 0.25), -1)

            else:
                print('расчет скидки с промокодом  не верен')

    @allure.step('Авторизация с очисткой корзины, заполнение корзины, заполнение полей оформления заказа')
    def preview_payment(self):

        page = LoginPage()
        page.authorization()
        page.click(page.close_btn, "Закрыть профиль")
        time.sleep(5)
        page = CatalogPage()
        page.click(page.basket_btn, "Переход в корзину")

        page = CartPage()
        page.cart_delete()

        time.sleep(5)
        page.open_url('https://lime:lime123@lmdev.ru/')

        page = CatalogPage()
        page.basket_changes_products()
        page.click(page.basket_btn, "Переход в корзину")

        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click(page.making_an_order_btn, "Клик кнопку оформления заказа")

        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")














