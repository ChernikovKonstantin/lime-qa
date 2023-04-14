import os
import time

import allure
import pytest

from pages.account import AccountPage
from pages.home import HomePage
from pages.login import LoginPage


@allure.feature("Тесты логина")
@pytest.mark.usefixtures("setup")
class TestLogin():


    @staticmethod
    @allure.title("Успешная авторизация")
    @allure.link("https://lmdev.testrail.io/index.php?/cases/view/441")

    def test_login_success():
        page = HomePage()
        time.sleep(6)
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()

        page = LoginPage()
        page.login(email=os.getenv("test_user"), password=os.getenv("password"))
        page.check_logout_btn_is_visible()

    @staticmethod
    @allure.title("Не успешая авторизация")
    def test_login_fail():
        page = HomePage()
        page.click_account_btn()

        page = AccountPage()
        page.click_enter_btn()
        time.sleep(3)

        page = LoginPage()
        page.login(email="qwerty@qwerty.qwerty", password=os.getenv("password"))
        page.check_login_error()


    @staticmethod
    @allure.title("Успешная регистрация")
    def test_registration_success():
        page = HomePage()

        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields()
        page = LoginPage()
        page.check_logout_btn_is_visible()

        time.sleep(3)

    @staticmethod
    @allure.title("Регистрация без чек-бокса рассылки")
    def test_registration_none_mailing():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.fill_registration_fields_none_mailing()
        time.sleep(3)
        page = LoginPage()
        page.check_logout_btn_is_visible()

        time.sleep(3)

    @staticmethod
    @allure.title("Проверка валидности поля email")
    def test_field_email():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_field_email()

    @staticmethod
    @allure.title("Проверка валидности поля номера телефона")
    def test_field_phone():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_field_phone_number()

    @staticmethod
    @allure.title("Проверка валидности поля Ваше имя")
    def test_field_name():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_field_name()




    @staticmethod
    @allure.title("Проверка валидности поля Ваша фамилия")
    def test_field_surname():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_field_surname()

    @staticmethod
    @allure.title("Проверка валидности поля Пароль")
    def test_field_password():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_field_password()

    @staticmethod
    @allure.title("Проверка валидности поля Повтор пароля")
    def test_field_repeat_password():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_field_repeat_password()

    @staticmethod
    @allure.title("Проверка совпадения паролей")
    def test_matching_password():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_field_matching_password()

    @staticmethod
    @allure.title("Проверка ссылки условий")
    def test_link_conditions():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.registration_link_conditions()




    @staticmethod
    @allure.title("Проверка ошибок полей при неуспешной регистрации")
    def test_registration_errors():
        page = HomePage()
        page.click_account_btn()
        page.click_registration_btn()
        page.click_registration_btn()

        list = page.get_text_error()
        print(list)
        #print(*list, sep="\n", end="\n\n")
        assert list[0] == ('поле обязательно для заполнения'), print('Некорректный текст ошибки регистрации')
        assert list[1] == ('некорректный e-mail'), print('Некорректный текст ошибки регистрации')
        assert list[2] == ('некорректный номер телефона'), print('Некорректный текст ошибки регистрации')
        assert list[3] == ('поле обязательно для заполнения'), print('Некорректный текст ошибки регистрации')
        assert list[4] == ('поле обязательно для заполнения'), print('Некорректный текст ошибки регистрации')
        assert list[5] == ('поле обязательно для заполнения'), print('Некорректный текст ошибки регистрации')
        assert list[6] == ('поле обязательно для заполнения'), print('Некорректный текст ошибки регистрации')
        assert list[7] == ('пароль должен быть не менее 6 символов'), print('Некорректный текст ошибки регистрации')
        assert list[8] == ('поле обязательно для заполнения'), print('Некорректный текст ошибки регистрации')
        assert list[9] == ('пароль должен быть не менее 6 символов'), print('Некорректный текст ошибки регистрации')














