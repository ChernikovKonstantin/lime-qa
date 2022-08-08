import json
import os

import allure
import pytest
from selene import config
from selene.api import browser
from seleniumwire import webdriver

from data import base_dir
from pages.base import BasePage


def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")
    prefs = {"download.default_directory": f"{base_dir}/downloads"}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    browser.set_driver(driver)
    driver.maximize_window()
    config.timeout = 10
    BasePage().open_url(os.getenv("base_url"))
    return driver


def browser_teardown(driver):
    driver.quit()


@pytest.fixture()
def setup():
    driver = setup_browser()
    yield
    browser_teardown(driver)


def pytest_exception_interact():
    allure.attach(
        name="Скринтшот",
        body=browser.driver.get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG,
    )
    console_log = browser.driver.get_log("browser")
    if not console_log:
        pass
    else:
        try:
            # attach a log file
            allure.attach(json.dumps(console_log), name="Логи консоли", attachment_type=allure.attachment_type.JSON)
        except:
            pass