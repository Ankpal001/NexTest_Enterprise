from config.config import LOGIN_URL
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        super().__init__(driver)
    def open_login_page(self):
        self.open(LOGIN_URL)
    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)