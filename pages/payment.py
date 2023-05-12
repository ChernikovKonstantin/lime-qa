import os
import time
import re

import allure
from selene.api import be, have, s
from selene.support.shared.jquery_style import ss

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
    to_pay_btn = s("//button[@tabindex='15']")
    to_pay_btn_disabled = s("//button[@class ='btn btn-block _disabled']")
    to_pay_btn_string = "//button[@class ='btn btn-block']"
    success_btn = s("//button[@class = 'button button_primary']")
    success_btn_string = "//button[@class = 'button button_primary']"
    success_btn_fault = s("//button[@class='button button_secondary']")
    success_btn_fault_string = "//button[@class='button button_secondary']"

    title_thank_you_page_text = s("//div[contains(text(),'Спасибо!')]")
    dropdown_quantity_product_on_payment = s("//div[@class='DropdownList__container DropdownList__inline']")
    # dropdown_quantity_product = s("(//div[@class='SvgIcon'])[2]/child::*")
    dropdown_quantity_product_select_5_on_payment = s("(//span[@class='DropdownList__title'])[5]")
    dropdown_quantity_product_select_1_on_payment = s("(//span[@class='DropdownList__title'])[1]")
    error_card_payment = s('// div[contains(text(), "ОПЛАТА НЕ ПРОШЛА: Свяжитесь с вашим банком или воспользуйтесь другой картой")]')
    error_card_payment_string = '// div[contains(text(), "ОПЛАТА НЕ ПРОШЛА: Свяжитесь с вашим банком или воспользуйтесь другой картой")]'

    #error_card_not_money = s('//div[contains(text(),"ОПЛАТА НЕ ПРОШЛА: Недостаточно средств на карте"]')
    error_card_not_money_string = '//div[@class="CustomerCartSummary__error"]'
    error_card_not_not_valid_card = '//div[contains (text(), "Неправильный номер карты")]'
    block_product = ss("//div[@class='CartTable__row']")
    message_out_of_stock = ss('//p[contains(text(), "Нет в наличии")]')
    button_del = s('//div[@class="SvgIcon IButtonIcon"]/child::*')
    button_del2 = s("//p[@class='CartTable__error']/ancestor::div[@class='CartTable__name']/following-sibling::button//div[@class='SvgIcon IButtonIcon']/child::*")





    #locators_delivery

    type_of_delivery_courier = s("//span[contains(text(), 'Доставка курьером')]")
    type_of_delivery_self = s("//span[contains(text(), 'Самовывоз из магазина')]")
    type_of_delivery_pic_point = s("//span[contains(text(), 'Пункты выдачи')]")
    point_self_and_pic_point_delivery = s("//div[@class='PickPointSelector__item']")
    button_choise_point = s('//button[@class="btn btn-block"]')

    # locators_type_payment
    type_of_payment_card = s("//span[contains(text(), 'Оплата картой онлайн')]")
    type_of_payment_gift_card = s("//span[contains(text(), 'Подарочной картой')]")
    type_of_payment_receiving = s("//span[contains(text(), 'При получении')]")
    string_data_card = '//div[contains(text(), "Данные вашей карты visa/mastercard/мир")]'





    # locators for promocode

    price_finally_block_cart_text = s("//span[@class='sale']") # цена с промо в блоке корзина
    price_finally_block_cart_text_string = "//span[@class='sale']"
    icon_discount_percent_block_cart_text = s('//span[@class="percent"]') # иконка процента промо
    icon_discount_percent_block_cart_text_string = '//span[@class="percent"]'
    discount_string = '//div[contains(text(), " Скидка на заказ")]'# строка Скидка на заказ
    price_discount_text = s('(//div[@class="CustomerCartSummary__value"])[3]/span')# сумма скидки
    price_without_discount_text = s('(//div[@class="CustomerCartSummary__value"])[2]/span')# итоговая сумма без промокода
    price_finally_text = s('(//div[@class="CustomerCartSummary__value"])[5]/span')# Итого
    price_finally_text_witout_discount = s('(//div[@class="CustomerCartSummary__value"])[4]/span')  # Итого при отсутсвии скидки
    promo_code_error = s("//div[contains(text(), 'промокод не найден')]")  # ошибка промокода
    promo_code_error_string = "//div[contains(text(), 'промокод не найден')]"  #ошибка промокода строка






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
        # time.sleep(3)
        # self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        # self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        # self.set_text(self.card_holder_field, "tester", "Владелец карты")
        # self.set_text(self.security_code_field, "123", "Код безопасности")
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


    @allure.step('Суммы полей заказа с промокодом')
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

    @allure.step('Проверка суммы заказа с учетом промо')
    def sum_order_with_discount(self):
        self.wait_element(self.discount_string)
        self.wait_element(self.icon_discount_percent_block_cart_text_string)
        price_result_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_block_cart_text, 'Получение итоговой суммы заказа из блока Корзина'))))
        total_price = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промокода'))))
        price_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text, 'Сумма скидки по промокоду, с округлением в большую сторону')))),-1)
        price_result = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text, 'Получение итоговой суммы заказа'))))
        icon_discount_percent_block_cart = (int(re.sub('[^0-9]', "", self.get_element_text(self.icon_discount_percent_block_cart_text, 'Получение процента скидки'))))
        price_discount_icon = round(total_price * (icon_discount_percent_block_cart / 100), -1)


        #return price_finally_block_cart, price_without_discount, price_discount, price_finally, icon_discount_percent_block_cart, price_discount_icon


        self.assert_check_expressions((price_result + price_discount),total_price, ' Ошибка проверки: Σ без промо = Σ итог в блоке корзина + Σ промокод')
        self.assert_check_expressions((price_result_block_cart + price_discount), total_price, 'Ошибка проверки: Σ без промо = Σ итог в строке Общая стоимость товаров + Σ промокод')
        self.assert_check_expressions((total_price - price_discount_icon), price_result_block_cart, 'Ошибка проверки: Σ без промо - (Σ без промо х %скидки) = Σ итог в строке Общая стоимость товаров')

    @allure.step('Проверка суммы заказа с учетом промо, несколько товаров')
    def sum_order_with_discount_many(self):
        self.wait_element(self.discount_string)
        self.wait_element(self.icon_discount_percent_block_cart_text_string)

        total_price = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text,
                                                                      'Получение суммы Общая стоимость товаров без промокода'))))
        price_discount = round((int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text,
                                                                               'Сумма скидки по промокоду, с округлением в большую сторону')))),
                               -1)
        price_result = (int(re.sub('[^0-9]', "",
                                   self.get_element_text(self.price_finally_text, 'Получение итоговой суммы заказа, с учетом скидки'))))
        icon_discount_percent_block_cart = (int(re.sub('[^0-9]', "",
                                                       self.get_element_text(self.icon_discount_percent_block_cart_text,
                                                                             'Получение процента скидки'))))
        price_discount_icon = round(total_price * (icon_discount_percent_block_cart / 100), -1)

        # return price_finally_block_cart, price_without_discount, price_discount, price_finally, icon_discount_percent_block_cart, price_discount_icon

        self.assert_check_expressions((price_result + price_discount), total_price,
                                      ' Ошибка проверки: Σ без промо = Σ итог в строке Общая стоимость товаров + Σ промокод')

        self.assert_check_expressions((total_price - price_discount_icon), price_result,
                                      'Ошибка проверки: Σ без промо - (Σ без промо х %скидки) = Σ итог в строке Общая стоимость товаров')

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

    @allure.step('Проверка полей  с не валидным промо')
    def check_payment_promo_not_valid(self):
        self.wait_element_assure(self.promo_code_error)
        self.wait_element_not_visible(self.discount_string)
        self.wait_element_not_visible(self.price_finally_block_cart_text_string)
        self.wait_element_not_visible(self.icon_discount_percent_block_cart_text_string)

        self.wait_element_assure(self.to_pay_btn)
        self.click(self.to_pay_btn, " оплата заказа")
        self.wait_element_assure(self.promo_code_error)

    @allure.step('Проверка отсутсвия элементов скидки с проверкой сумм')
    def check_without_discount(self):
        self.wait_element_not_visible(self.discount_string)
        self.wait_element_not_visible(self.price_finally_block_cart_text_string)
        self.wait_element_not_visible(self.icon_discount_percent_block_cart_text_string)

        price_finally = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text_witout_discount,
                                                                        'Получение суммы заказа при 0 скидке'))))
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text,
                                                                                 'Получение суммы заказа без промо'))))
        self.assert_check_expressions(price_without_discount, price_finally, " промокод применен неверно")



    @allure.step('Цикл проверки промокодов')
    def cycle_type_promo_code(self):

        list_promo = ['XHGFAH', 'SOTRUDN25']
        promo_0 = 'LIMEPR'

        for i in range(len(list_promo)):

            self.set_text(self.promo_code_field, list_promo[i], "Установка промокода в поле")

            time.sleep(2)
            self.wait_element_assure(self.icon_discount_percent_block_cart_text)

            percent_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.icon_discount_percent_block_cart_text, 'Извлечение процента из элемента процент скидки'))))

            price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промо'))))

            price_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text, 'Получение суммы скидки'))))

            if percent_discount == 5:

                self.assert_check_expressions(price_discount, (round((price_without_discount * 0.05), -1)),' не пройдена Проверка скидки 5%')
                #assert price_discount == round((price_without_discount * 0.05), -1)

            elif percent_discount == 10:
                self.assert_check_expressions(price_discount, (round((price_without_discount * 0.1), -1)),' не пройдена Проверка скидки 10%')
                #assert price_discount == round((price_without_discount * 0.1), -1)

            elif percent_discount == 25:
                self.assert_check_expressions(price_discount, (round((price_without_discount * 0.25), -1)),' не пройденаПроверка скидки 25%')
                #assert price_discount == round((price_without_discount * 0.25), -1)

            else:
                print('расчет скидки с промокодом  не верен')

        self.set_text(self.promo_code_field, promo_0, "Установка промокода с 0 скидкой в поле")
        self.wait_element_not_visible(self.discount_string)
        self.wait_element_not_visible(self.price_finally_block_cart_text_string)
        self.wait_element_not_visible(self.icon_discount_percent_block_cart_text_string)
        price_finally = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text_witout_discount, 'Получение суммы заказа при 0 скидке'))))
        self.assert_check_expressions(price_without_discount, price_finally, " промокод применен неверно")




    @allure.step('Авторизация с очисткой корзины, заполнение корзины 1 товаром,проверка наличия товаров, заполнение полей оформления заказа')
    def preview_payment(self):

        page = LoginPage()
        page.authorization()
        page.wait_element_assure(page.close_btn)
        page.click(page.close_btn, "Закрыть профиль")

        page = CatalogPage()
        page.wait_element_assure(page.basket_btn)
        time.sleep(3)
        page.click(page.basket_btn, "Переход в корзину")

        page = CartPage()
        page.cart_delete()

        page.open_url(os.getenv('base_url'))

        page = CatalogPage()
        page.basket_changes_products_1399()
        #page.basket_multiple_products()
        page.click(page.basket_btn, "Переход в корзину")

        self.check_product_for_order()

        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click(page.making_an_order_btn, "Клик кнопку оформления заказа")

        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")

    @allure.step('Авторизация с очисткой корзины, заполнение корзины несколькими товарами, проверка наличия товаров, заполнение полей оформления заказа')
    def preview_payment_many_products(self):

        page = LoginPage()
        page.authorization()
        page.wait_element_assure(page.close_btn)
        page.click(page.close_btn, "Закрыть профиль")

        page = CatalogPage()
        page.wait_element_assure(page.basket_btn)
        time.sleep(3)
        page.click(page.basket_btn, "Переход в корзину")

        page = CartPage()
        page.cart_delete()

        page.open_url(os.getenv('base_url'))

        page = CatalogPage()
        #page.basket_changes_products_1399()
        page.basket_add_many_products()
        page.click(page.basket_btn, "Переход в корзину")

        self.check_product_for_order()

        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click(page.making_an_order_btn, "Клик кнопку оформления заказа")

        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")

    @allure.step(
        'Авторизация с очисткой корзины, заполнение корзины 1 товаром и увеличение до 5,проверка наличия товаров, заполнение полей оформления заказа')
    def preview_payment_6000(self):

        page = LoginPage()
        page.authorization()
        page.wait_element_assure(page.close_btn)
        page.click(page.close_btn, "Закрыть профиль")

        page = CatalogPage()
        page.wait_element_assure(page.basket_btn)
        time.sleep(3)
        page.click(page.basket_btn, "Переход в корзину")

        page = CartPage()
        page.cart_delete()

        page.open_url(os.getenv('base_url'))

        page = CatalogPage()
        page.basket_changes_products_1399()
        # page.basket_multiple_products()
        page.click(page.basket_btn, "Переход в корзину")
        self.change_value_products_in_payment_5_unit()

        self.check_product_for_order()

        page = CartPage()
        page.wait_element(page.making_an_order_btn_string)
        page.click(page.making_an_order_btn, "Клик кнопку оформления заказа")

        self.set_text(self.card_number_field, "4242 4242 4242 4242", " Номер карты")
        self.set_text(self.validity_period_field, "12/24", "Дата окончания срока действия")
        self.set_text(self.card_holder_field, "tester", "Владелец карты")
        self.set_text(self.security_code_field, "123", "Код безопасности")

    @allure.step("Проверка наличия товара")
    def check_product_for_order(self):

        try:
            #if len(self.message_out_of_stock) > 0:
            for i in range(len(self.message_out_of_stock)):

                self.click(self.button_del2, " кнопку удаления заказа")
                time.sleep(2)
        except:
            pass

    @allure.step("Заполнение поля промокодом 0")
    def enter_valid_promo_0(self):
        self.set_text(self.promo_code_field, "LIMEPR", "Промо код 0")

    @allure.step("Заполнение поля промокодом 10%")
    def enter_valid_promo_10(self):
        self.set_text(self.promo_code_field, "XHGFAH", "Промо код 10%")

    @allure.step("Заполнение поля промокодом 25%")
    def enter_valid_promo_25(self):
        self.set_text(self.promo_code_field, "SOTRUDN25", "Промо код 25%")

    @allure.step("Оплата при заполненных полях")
    def pay_order(self):

        self.wait_element_assure(self.to_pay_btn)
        self.click(self.to_pay_btn, "кнопка оплаты")

        self.wait_element_assure(self.success_btn)
        self.click(self.success_btn, " кнопка опалты Удачно")

        self.wait_element_assure(self.title_thank_you_page_text)

        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, " получение текста элемента")

        self.assert_check_expressions("СПАСИБО!", title_thank_you_page, " нет сообщения об успешной оплате")

    @allure.step("Оплата при заполненных полях при постоплате")
    def pay_order_post_payment(self):

        self.wait_element_assure(self.to_pay_btn)
        self.click(self.to_pay_btn, "кнопка Закзать")
        self.wait_element_assure(self.title_thank_you_page_text)
        title_thank_you_page = self.get_element_text(self.title_thank_you_page_text, " получение текста элемента")
        self.assert_check_expressions("СПАСИБО!", title_thank_you_page, " нет сообщения об успешной оплате")

    @allure.step("Оплата при заполненных полях без проверок")
    def pay_order_without_check(self):

        self.wait_element_assure(self.to_pay_btn)
        self.click(self.to_pay_btn, "кнопка оплаты")

        self.wait_element_assure(self.success_btn)
        self.click(self.success_btn, " кнопка опалты Удачно")


    @allure.step("Не удачная оплата")
    def pay_order_error(self):

        self.wait_element_assure(self.to_pay_btn)
        self.click(self.to_pay_btn, "кнопка оплаты")

        self.wait_element_assure(self.success_btn_fault)
        self.click(self.success_btn_fault, " кнопка опалты Не удачно")

        self.wait_element_assure(self.error_card_payment)

        message_error = self.get_element_text(self.error_card_payment, " получение текста элемента")

        self.assert_check_expressions("ОПЛАТА НЕ ПРОШЛА: Свяжитесь с вашим банком или воспользуйтесь другой картой", message_error, " нет сообщения о неуспешной оплате")




    @allure.step('Получение значений полей скидки')
    def extract_discount_value(self):

        self.wait_element_assure(self.icon_discount_percent_block_cart_text)

        percent_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.icon_discount_percent_block_cart_text, 'Извлечение процента из элемента процент скидки'))))
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text, 'Получение суммы заказа без промо'))))
        price_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_discount_text, 'Получение суммы скидки'))))

        return percent_discount, price_without_discount, price_discount

    @allure.step('Прверка промокода 0 при заказе 6000')
    def check_discount_0_6000(self):
        percent_discount, price_without_discount, price_discount = self.extract_discount_value()
        self.assert_check_expressions(price_discount, (round((price_without_discount * 0.05), -1)), ' не пройдена Проверка скидки 5%')






    @allure.step('Прверка суммы скидки 0')
    def check_discount_0(self):


        price_finally = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text_witout_discount,
                                                                        'Получение суммы заказа при 0 скидке'))))
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text,
                                                                                 'Получение суммы заказа без промо'))))
        self.assert_check_expressions(price_without_discount, price_finally, " промокод применен неверно")



        #     self.assert_check_expressions(price_discount, (round((price_without_discount * 0.05), -1)),
        #                                   ' не пройдена Проверка скидки 5%')
        #     # assert price_discount == round((price_without_discount * 0.05), -1)
        #
        # elif percent_discount == 10:
        #     self.assert_check_expressions(price_discount, (round((price_without_discount * 0.1), -1)),
        #                                   ' не пройдена Проверка скидки 10%')
        #     # assert price_discount == round((price_without_discount * 0.1), -1)
        #
        # elif percent_discount == 25:
        #     self.assert_check_expressions(price_discount, (round((price_without_discount * 0.25), -1)),
        #                                   ' не пройденаПроверка скидки 25%')
        #     # assert price_discount == round((price_without_discount * 0.25), -1)
        #
        # else:
        #     print('расчет скидки с промокодом  не верен')

    @allure.step('Проверка  элементов при скидке 0')
    def extract_discount_value(self):
        self.wait_element_not_visible(self.discount_string)
        self.wait_element_not_visible(self.price_finally_block_cart_text_string)
        self.wait_element_not_visible(self.icon_discount_percent_block_cart_text_string)
        price_finally = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_finally_text_witout_discount,
                                                                        'Получение суммы заказа при 0 скидке'))))
        price_without_discount = (int(re.sub('[^0-9]', "", self.get_element_text(self.price_without_discount_text,
                                                                                 'Получение суммы заказа без промо'))))
        self.assert_check_expressions(price_without_discount, price_finally, " промокод применен неверно")





















