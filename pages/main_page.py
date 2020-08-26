from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    def go_to_mail(self):
        mail_link = self.driver.find_element(*MainPageLocators.MAIL_LINK)
        mail_link.click()
        mail_window = self.driver.window_handles[1]
        self.driver.switch_to.window(mail_window)

    def go_to_video(self):
        try:
            nav_video_link = self.driver.find_element(*MainPageLocators.NAV_VIDEO_LINK)
        except NoSuchElementException:
            nav_video_link = self.driver.find_element(*MainPageLocators.NAV_VIDEO_LINK_V2)
        nav_video_link.click()
        video_window = self.driver.window_handles[1]
        self.driver.switch_to.window(video_window)

    def go_to_images(self):
        try:
            nav_images_link = self.driver.find_element(*MainPageLocators.NAV_IMAGES_LINK)
        except NoSuchElementException:
            nav_images_link = self.driver.find_element(*MainPageLocators.NAV_IMAGES_LINK_V2)
        nav_images_link.click()
        image_window = self.driver.window_handles[1]
        self.driver.switch_to.window(image_window)

    def go_to_news(self):
        try:
            nav_news_link = self.driver.find_element(*MainPageLocators.NAV_NEWS_LINK)
        except NoSuchElementException:
            nav_news_link = self.driver.find_element(*MainPageLocators.NAV_NEWS_LINK_V2)
        nav_news_link.click()
        news_window = self.driver.window_handles[1]
        self.driver.switch_to.window(news_window)

    def go_to_maps(self):
        try:
            nav_maps_link = self.driver.find_element(*MainPageLocators.NAV_MAPS_LINK)
        except NoSuchElementException:
            nav_maps_link = self.driver.find_element(*MainPageLocators.NAV_MAPS_LINK_V2)
        nav_maps_link.click()
        maps_window = self.driver.window_handles[1]
        self.driver.switch_to.window(maps_window)

    def go_to_market(self):
        try:
            nav_market_link = self.driver.find_element(*MainPageLocators.NAV_MARKET_LINK)
        except NoSuchElementException:
            nav_market_link = self.driver.find_element(*MainPageLocators.NAV_MARKET_LINK_V2)
        nav_market_link.click()
        market_window = self.driver.window_handles[1]
        self.driver.switch_to.window(market_window)

    def go_to_translate(self):
        try:
            nav_translate_link = self.driver.find_element(*MainPageLocators.NAV_TRANSLATE_LINK)
        except NoSuchElementException:
            nav_translate_link = self.driver.find_element(*MainPageLocators.NAV_TRANSLATE_LINK_V2)
        nav_translate_link.click()
        translate_window = self.driver.window_handles[1]
        self.driver.switch_to.window(translate_window)

    def go_to_music(self):
        try:
            nav_music_link = self.driver.find_element(*MainPageLocators.NAV_MUSIC_LINK)
        except NoSuchElementException:
            nav_music_link = self.driver.find_element(*MainPageLocators.NAV_MUSIC_LINK_V2)
        nav_music_link.click()
        music_window = self.driver.window_handles[1]
        self.driver.switch_to.window(music_window)

    def go_to_lang_page(self):
        lang_link = self.driver.find_element(*MainPageLocators.LANG_LINK)
        lang_link.click()
        lang_link_more = self.driver.find_element(*MainPageLocators.LANG_MORE_LINK)
        lang_link_more.click()
