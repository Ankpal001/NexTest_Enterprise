from config.config import EXPLICIT_WAIT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class BasePage:
    def __init__(self, driver, timeout=EXPLICIT_WAIT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def open(self, url):
        self.logger.info("Opening URL: %s", url)
        self.driver.get(url)

    def click(self, locator):
        self.logger.info("Clicking element: %s", locator)
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        self.logger.info("Entering text into element: %s", locator)
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.logger.info("Reading text from element: %s", locator)
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
