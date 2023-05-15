import random
import time
from random import randint
from telnetlib import EC

import allure
from selene import wait
from selene.api import browser
from selene.api import *
from pages.base import BasePage


class HomePage(BasePage):
    # Locators

    account_btn = s("//a[@href = '/ru_ru/#lk' and @class = 'btn-control']")

    registration_btn = s("//button[contains(text(),'Зарегистрироваться')]")
    email_field = s("//input[@type='email' and @placeholder='E-mail']")
    phone_number_field = s("//input[@class= 'vti__input']")
    name_field = s("//input[@placeholder='Ваше имя']")
    name_field_2 = s("//input[@placeholder='Имя']")
    surname_name_field = s("//input[@placeholder='Фамилия']")

    new_password_field = s("//input[@placeholder='Новый пароль']")
    repeat_the_password_field = s("//input[@placeholder='Повторите пароль']")
    checkbox_mailing = s("//*[@class='checkbox__indicator']")
    link_conditions = s("//a[@href='/docs/offerta.pdf']")

    # Liocators Errores Registration form
    message_error_email_text = s("(//*[@class='FormGroup__helper'])[1]/div[1]")
    #message_error_email_text_var = s("(//input[@placeholder='E-mail']/ancestor::div[@class='FormGroup hasError']//div[@class='FormGroup__helper']/div)
    message_error_email_text_var_string = "//div[contains(text(),'некорректный e-mail')]"
    message_error_email_text_var = s(message_error_email_text_var_string)

    message_error_email_text2 = s("(//*[@class='FormGroup__helper'])[1]/div[2]")

    message_error_phone_text = s("(//*[@class='FormGroup__helper'])[2]/div[1]")
    message_error_phone_text_var_string = "//div[contains(text(),'некорректный номер телефона')]"
    message_error_phone_text_var = s(message_error_phone_text_var_string)

    message_error_phone_text2 = s("(//*[@class='FormGroup__helper'])[2]/div[2]")

    message_error_name_text = s("(//*[@class='FormGroup__helper'])[3]/div[1]")
    message_error_name_text_var_string = "//div[contains(text(),'недопустимое имя')]"
    message_error_name_text_var = s(message_error_name_text_var_string)

    message_error_surname_text = s("(//*[@class='FormGroup__helper'])[4]/div[1]")
    message_error_surname_text_var_string = "//div[contains(text(),'недопустимая фамилия')]"
    message_error_surname_text_var = s(message_error_surname_text_var_string)

    message_error_password_text = s("(//*[@class='FormGroup__helper'])[5]/div[1]")
    message_error_password_text_var_string = "//div[contains(text(),'пароль должен быть не менее 6 символов')]"
    message_error_password_text_var = s(message_error_password_text_var_string)

    message_error_password_text2 = s("(//*[@class='FormGroup__helper'])[5]/div[2]")

    message_error_repeat_password_text = s("(//*[@class='FormGroup__helper'])[6]/div[1]")
    message_error_repeat_password_text_smoke = s("(//*[@class='FormGroup__helper'])[3]/div[1]")
    message_error_repeat_password_text_var_string = "//div[contains(text(),'недопустимый пароль')]"
    message_error_repeat_password_text_var = s(message_error_repeat_password_text_var_string)

    message_error_repeat_password_text2 = s("(//*[@class='FormGroup__helper'])[6]/div[2]")

    message_error_password_miss_string = "//div[contains(text(),'введенные пароли не совпадают')]"
    #message_error_password_miss = s(message_error_password_miss_string)
    message_error_password_miss = s("//div[contains(text(),'введенные пароли не совпадают')]")
    # message_error_password_miss = s("//*[@id=\"app\"]/div[1]/div/div/div/div/form/div[8]/div[2]/div")
    # Methods
    @allure.step("Нажать Аккаунт")
    def click_account_btn(self):
        self.account_btn.click()

    @allure.step("Нажать Зарегистрироваться")
    def click_registration_btn(self):
        self.registration_btn.click()


    @allure.step("Заполнение всех полей регистрации")
    def fill_registration_fields(self):
        self.set_text(self.email_field, 'test' + str(randint(0, 9999)) + '@test.ru', " почта")
        self.set_text(self.phone_number_field, "+79998887755", " номер телефона")
        self.set_text(self.name_field, "Test", " ИМЯ")
        self.set_text(self.surname_name_field, "Testerov", " ФАМИЛИЯ")
        self.set_text(self.new_password_field, "123456789", " НОВЫЙ ПАРОЛЬ")
        self.set_text(self.repeat_the_password_field, "123456789", " ПОДТВЕРДИТЕ ПАРОЛЬ")
        time.sleep(10)
        self.registration_btn.click()

    @allure.step("Заполнение полей регистрации Smoke")
    def fill_registration_fields_smoke(self):
        self.set_text(self.email_field, 'qwer', " почта")
        self.set_text(self.phone_number_field, "+7", " номер телефона")
        self.set_text(self.new_password_field, "123456789", " НОВЫЙ ПАРОЛЬ")
        self.set_text(self.repeat_the_password_field, "12345678", " ПОДТВЕРДИТЕ ПАРОЛЬ")
        time.sleep(10)
        self.registration_btn.click()

    @allure.step("Заполнение всех полей регистрации со снятием чек-бокса рассылки")
    def fill_registration_fields_none_mailing(self):
        self.set_text(self.email_field, 'test' + str(randint(0, 9999)) + '@test.ru', " почта")
        self.set_text(self.phone_number_field, "+79998887755", " номер телефона")
        self.set_text(self.name_field, "Test", " ИМЯ")
        self.set_text(self.surname_name_field, "Testerov", " ФАМИЛИЯ")
        self.set_text(self.new_password_field, "123456789", " НОВЫЙ ПАРОЛЬ")
        self.set_text(self.repeat_the_password_field, "123456789", " ПОДТВЕРДИТЕ ПАРОЛЬ")
        self.checkbox_mailing.click()
        self.registration_btn.click()

    @allure.step("Ошибки полей формы регистрации")
    def get_text_error(self):
        message_error_email = self.get_element_text(self.message_error_email_text, "")
        message_error_email2 = self.get_element_text(self.message_error_email_text2, "")
        message_error_phone = self.get_element_text(self.message_error_phone_text, "")
        message_error_phone2 = self.get_element_text(self.message_error_phone_text2, "")
        message_error_name = self.get_element_text(self.message_error_name_text, "")
        message_error_surname = self.get_element_text(self.message_error_surname_text, "")
        message_error_password = self.get_element_text(self.message_error_password_text, "")
        message_error_password2 = self.get_element_text(self.message_error_password_text2, "")
        message_error_repeat_password = self.get_element_text(self.message_error_repeat_password_text, "")
        message_error_repeat_password2 = self.get_element_text(self.message_error_repeat_password_text2, "")

        return message_error_email, message_error_email2, message_error_phone, message_error_phone2, message_error_name, \
            message_error_surname, message_error_password, message_error_password2, message_error_repeat_password, \
            message_error_repeat_password2

    @allure.step("Ошибки полей формы регистрации Smoke")
    def get_text_error_smoke(self):
        message_error_email = self.get_element_text(self.message_error_email_text, "")
        message_error_phone = self.get_element_text(self.message_error_phone_text, "")
        message_error_repeat_password_smoke = self.get_element_text(self.message_error_repeat_password_text_smoke, "")

        return message_error_email, message_error_phone, message_error_repeat_password_smoke

    @allure.step("Валидация поля Email")
    def registration_field_email(self):
        public_string_not_valid_mail = ('mail', 'mail.mail', 'mail@mail', 'mail@mail.r', 'mail@', 'мейл@mail.ru', 'mail@ma il.ru')
        #print(len(public_string_not_valid_mail))
        for i in range(len(public_string_not_valid_mail)):
            self.set_text(self.email_field, public_string_not_valid_mail[i], "")
            time.sleep(5) # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            message_error = self.get_element_text(self.message_error_email_text_var, "Текст ошибки поля  пароль не верный или текст отсутствует")
            time.sleep(2)
            assert message_error == "некорректный e-mail", print("Ошибка сообщения. Текст ошибки: " + message_error)

        public_string_valid_mail = (('mail' + str(randint(0, 9999)) + 'mail.ru'), (' mail' + str(randint(0, 9999)) + 'mail.ru'),
            ('mail' + str(randint(0, 9999)) + 'mail.ru '))
        for i in range(len(public_string_valid_mail)):
                self.set_text(self.email_field, public_string_valid_mail[i], "")
                time.sleep(5)  # убрать после фикса бага
                self.registration_btn.click()
                time.sleep(2)
                self.wait_element(self.message_error_email_text_var_string)
                time.sleep(2)
        print("end")



    @allure.step("Валидация поля Номер телефона")
    def registration_field_phone_number(self):

        public_string_not_vail_number = (999888776, 999888775, "9998887m")

        for i in range(len(public_string_not_vail_number)):
            self.set_text(self.phone_number_field, public_string_not_vail_number[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            message_error = self.get_element_text(self.message_error_phone_text_var, "Текст ошибки поля  пароль не верный или текст отсутствует")
            time.sleep(2)
            assert message_error == "некорректный номер телефона", print("Ошибка сообщения. Текст ошибки: " + message_error)

        public_string_valid_number = (9998887766, 9998887765)

        for i in range(len(public_string_valid_number)):
            self.set_text(self.phone_number_field, public_string_valid_number[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            self.wait_element(self.message_error_phone_text_var_string)
            time.sleep(2)




    @allure.step("Валидация поля Ваше имя")
    def registration_field_name(self):

        public_string_not_valid_name = ('ivan,.!"№%:;()_-+=?/|\@#$^&*<>{}[', 12345, " ", )

        for i in range(len(public_string_not_valid_name)):
            self.set_text(self.name_field, public_string_not_valid_name[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            message_error = self.get_element_text(self.message_error_name_text_var, "Текст ошибки поля  пароль не верный или текст отсутствует")
            time.sleep(2)
            assert message_error == "некорректное имя", print("Ошибка сообщения. Текст ошибки: " + message_error)

        public_string_valid_name = ("Ivan123", "h", "п", "Иван123")

        for i in range(len(public_string_valid_name)):
            self.set_text(self.name_field, public_string_valid_name[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            self.wait_element(self.message_error_name_text_var_string)
            time.sleep(2)

    @allure.step("Валидация поля Ваша фамилия")
    def registration_field_surname(self):

        public_string_not_valid_surname = ('ivanov,.!"№%:;()_-+=?/|\@#$^&*<>{}[', 12345, " ", "N")

        for i in range(len(public_string_not_valid_surname)):
            self.set_text(self.surname_name_field, public_string_not_valid_surname[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            message_error = self.get_element_text(self.message_error_surname_text_var, "Текст ошибки поля  пароль не верный или текст отсутствует")
            time.sleep(2)
            assert message_error == "недопустимое имя", print("Ошибка сообщения. Текст ошибки: " + message_error)

        public_string_valid_surname = ("Ivan123", "h", "п", "Иван123")

        for i in range(len(public_string_valid_surname)):
            self.set_text(self.surname_name_field, public_string_valid_surname[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            self.wait_element(self.message_error_surname_text_var_string)
            time.sleep(2)


    @allure.step("Валидация поля Пароль")
    def registration_field_password(self):

        public_string_not_valid_password = ('wer23', 123)

        for i in range(len(public_string_not_valid_password)):
            self.set_text(self.new_password_field, public_string_not_valid_password[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            message_error = self.get_element_text(self.message_error_password_text_var, "Текст ошибки поля  пароль не верный или текст отсутствует")
            time.sleep(2)
            assert message_error == "пароль должен быть не менее 6 символов", print("Ошибка сообщения. Текст ошибки: " + message_error)

        public_string_valid_password = ("Ivano123", "123", "Иван_123", "Иван123")

        for i in range(len(public_string_valid_password)):
            self.set_text(self.new_password_field, public_string_valid_password[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            self.wait_element(self.message_error_password_text_var_string)
            time.sleep(2)

    @allure.step("Валидация поля Повторить Пароль")
    def registration_field_repeat_password(self):

        public_string_not_valid_repeat_password = ('wer23', 123)

        for i in range(len(public_string_not_valid_repeat_password)):
            self.set_text(self.repeat_the_password_field, public_string_not_valid_repeat_password[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            message_error = self.get_element_text(self.message_error_repeat_password_text_var, "Текст ошибки поля повторить пароль не верный или текст отсутствует")
            assert message_error == "пароль должен быть не менее 6 символов", print("Ошибка сообщения. Текст ошибки: " + message_error)


        public_string_valid_password = ("Ivanov123", "Иванов123", "Иванов123_", "Иванов123-")

        for i in range(len(public_string_valid_password)):
            self.set_text(self.repeat_the_password_field, public_string_valid_password[i], "")
            time.sleep(5)  # убрать после фикса бага
            self.registration_btn.click()
            time.sleep(2)
            page = BasePage
            page.wait_element(HomePage.message_error_repeat_password_text_var_string)
            time.sleep(2)

    @allure.step("Проверка соответсия паролей")
    def registration_field_matching_password(self):

        self.set_text(self.new_password_field, "password", "")
        self.set_text(self.repeat_the_password_field, "password2", "")
        self.registration_btn.click()
        message_error = self.get_element_text(self.message_error_password_miss, "Текст ошибки поля пароль не верный или текст отсутствует")
        assert message_error == "введенные пароли не совпадают", print("Ошибка сообщения. Текст ошибки: " + message_error)


        self.set_text(self.new_password_field, "password", "")
        self.set_text(self.repeat_the_password_field, "password", "")
        time.sleep(2)
        self.registration_btn.click()
        time.sleep(3)
        self.wait_element_not_visible(self.message_error_password_miss_string)


    @allure.step("Проверка ссылки условий использования")
    def registration_link_conditions(self):

        url_link_conditions = self.get_attribute(self.link_conditions, "href")
        print(url_link_conditions)
        assert url_link_conditions == ('https://nuxt-01.qa.lmdev.ru/docs/offerta.pdf'), print("Ссылка не верная")
        print(url_link_conditions)


