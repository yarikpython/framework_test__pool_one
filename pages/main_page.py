from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_mail(self):
        mail_link = self.driver.find_element(*MainPageLocators.MAIL_LINK)
        mail_link.click()

    def go_to_video(self):
        nav_video_link = self.driver.find_element(*MainPageLocators.NAV_VIDEO_LINK)
        nav_video_link.click()

    def go_to_images(self):
        nav_images_link = self.driver.find_element(*MainPageLocators.NAV_IMAGES_LINK)
        nav_images_link.click()

    def go_to_news(self):
        nav_news_link = self.driver.find_element(*MainPageLocators.NAV_NEWS_LINK)
        nav_news_link.click()

    def go_to_maps(self):
        nav_maps_link = self.driver.find_element(*MainPageLocators.NAV_MAPS_LINK)
        nav_maps_link.click()

    def go_to_market(self):
        nav_market_link = self.driver.find_element(*MainPageLocators.NAV_MARKET_LINK)
        nav_market_link.click()

    def go_to_translate(self):
        nav_translate_link = self.driver.find_element(*MainPageLocators.NAV_TRANSLATE_LINK)
        nav_translate_link.click()

    def go_to_music(self):
        nav_music_link = self.driver.find_element(*MainPageLocators.NAV_MUSIC_LINK)
        nav_music_link.click()

    def go_to_lang_page(self):
        lang_link = self.driver.find_element(*MainPageLocators.LANG_LINK)
        lang_link.click()
        lang_link_more = self.driver.find_element(*MainPageLocators.LANG_MORE_LINK)
        lang_link_more.click()
