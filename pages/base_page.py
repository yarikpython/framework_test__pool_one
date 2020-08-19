from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage:

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_lang(self):
        lang = self.driver.find_element_by_tag_name('html').get_attribute('lang')
        return lang
