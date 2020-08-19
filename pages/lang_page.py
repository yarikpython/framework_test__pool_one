import time

from .base_page import BasePage
from .locators import LangPageLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LangPage(BasePage):

    def choice_lang_en(self):
        self.driver.execute_script("select = document.getElementsByClassName('select__control')[0];\
                select.style.display='block';")
        select_lang = self.driver.find_element(*LangPageLocators.LANG_SELECT)
        select = Select(select_lang)
        select.select_by_value('en')

    def save_changes(self):
        save_button = self.driver.find_element(*LangPageLocators.SAVE_BUTTON)
        save_button.click()
