
import pytest
import allure

from pages.login_page import LoginPage
from utils.data_reader import read_json


LOGIN_TEST_DATA = read_json("login_data.json")


@allure.suite("UI Automation")
@allure.epic("Login Functionality")
@allure.feature("OpenCart Login")
@allure.story("Login Page")
@allure.title("Verify OpenCart login page opens")
def test_login_page_opens(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

    assert "Account Login" in driver.title


@pytest.mark.parametrize("test_data",LOGIN_TEST_DATA,ids=[item["test_case"] for item in LOGIN_TEST_DATA])
@allure.suite("UI Automation")
@allure.epic("Login Functionality")
@allure.feature("OpenCart Login")
@allure.story("Negative Login")
def test_invalid_login_shows_error(driver, test_data):
    allure.dynamic.title(test_data["test_case"])

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_email(test_data["email"])
    login_page.enter_password(test_data["password"])
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Warning" in error_message
