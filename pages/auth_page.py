from .base_page import BasePage
from .locators import AuthPageLocators
from selenium.webdriver.common.keys import Keys


class AuthPage(BasePage):

    def send_username(self, username: str):
        username_input = self.driver.find_element(*AuthPageLocators.INPUT_USERNAME)
        username_input.send_keys(username)
        username_input.send_keys(Keys.ENTER)

    def send_password(self, password: str):
        password_input = self.driver.find_element(*AuthPageLocators.INPUT_PASSWORD)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
