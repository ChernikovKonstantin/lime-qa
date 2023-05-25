
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
from pages.smoke import SmokePage
from selene.support.shared import browser

@allure.feature("Тест запуска")
#@pytest.mark.usefixtures("setup")
class TestStart:



    @allure.title("01")
    @pytest.mark.smoke(1)
    def test_start01(self):
        print("01")

    @allure.title("02")
    @pytest.mark.smoke(2)
    def test_start02(self):
        print("02")

    @allure.title("03")
    @pytest.mark.smoke(3)
    def test_start03(self):
        print("03")

    @allure.title("04")
    @pytest.mark.smoke
    def test_start04(self):
        print("04")

    @allure.title("05")
    @pytest.mark.smoke
    def test_start05(self):
        print("05")

    @allure.title("06")
    @pytest.mark.smoke
    def test_start06(self):
        print("06")

    @allure.title("07")
    @pytest.mark.smoke
    def test_start07(self):
        print("07")

    @allure.title("08")
    @pytest.mark.smoke
    def test_start08(self):
        print("08")

    @allure.title("09")
    @pytest.mark.smoke
    def test_start09(self):
        print("09")

    @allure.title("10")
    @pytest.mark.smoke
    def test_start10(self):
        print("10")

    @allure.title("11")
    @pytest.mark.smoke
    def test_start11(self):
        print("11")

    @allure.title("12")
    @pytest.mark.smoke
    def test_start12(self):
        print("12")

    @allure.title("13")
    @pytest.mark.smoke
    def test_start13(self):
        print("13")

    @allure.title("14")
    @pytest.mark.smoke
    def test_start14(self):
        print("14")

    @allure.title("15")
    @pytest.mark.smoke
    def test_start15(self):
        print("15")

    # @allure.title("01")
    # @pytest.mark.smoke
    # def test_start01(self):
    #     print("01")
    #
    # @allure.title("01")
    # @pytest.mark.smoke
    # def test_start01(self):
    #     print("01")
    #
    # @allure.title("01")
    # @pytest.mark.smoke
    # def test_start01(self):
    #     print("01")
    #
    # @allure.title("01")
    # @pytest.mark.smoke
    # def test_start01(self):
    #     print("01")
