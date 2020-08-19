from .base_page import BasePage
from .locators import YandexMailPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class YandexMailPage(BasePage):

    def get_username(self):
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.user-account>span.user-account__name'))).text
        return username

    def logout(self):
        username = self.driver.find_element(*YandexMailPageLocators.USERNAME)
        username.click()
        logout_link = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Выйти из аккаунта']")))
        logout_link.click()
