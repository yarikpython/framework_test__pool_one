from selenium.webdriver.common.by import By


class BasePageLocators:
    ALERT_COOKIE = (By.CLASS_NAME, 'lg-cc lg-cc_visible')
    BUTTON_ACCEPT_COOKIE = (By.CSS_SELECTOR, 'button.lg-cc__button lg-cc__button_type_action')


class MainPageLocators:
    MAIL_LINK = (By.CSS_SELECTOR, '[data-statlog="notifications.mail.logout.title"]')
    NAV_VIDEO_LINK = (By.CSS_SELECTOR, '[data-id="video"]')
    NAV_VIDEO_LINK_V2 = (By.XPATH, "//div[contains(text(), 'Видео')]")
    NAV_IMAGES_LINK = (By.CSS_SELECTOR, '[data-id="images"]')
    NAV_IMAGES_LINK_V2 = (By.XPATH, "//div[contains(text(), 'Картинки')]")
    NAV_NEWS_LINK = (By.CSS_SELECTOR, '[data-id="news"]')
    NAV_NEWS_LINK_V2 = (By.XPATH, "//div[contains(text(), 'Новости')]")
    NAV_MAPS_LINK = (By.CSS_SELECTOR, '[data-id="maps"]')
    NAV_MAPS_LINK_V2 = (By.XPATH, "//div[contains(text(), 'Карты')]")
    NAV_MARKET_LINK = (By.CSS_SELECTOR, '[data-id="market"]')
    NAV_MARKET_LINK_V2 = (By.XPATH, "//div[contains(text(), 'Маркет')]")
    NAV_TRANSLATE_LINK = (By.CSS_SELECTOR, '[data-id="translate"]')
    NAV_TRANSLATE_LINK_V2 = (By.XPATH, "//div[contains(text(), 'Переводчик')]")
    NAV_MUSIC_LINK = (By.CSS_SELECTOR, '[data-id="music"]')
    NAV_MUSIC_LINK_V2 = (By.XPATH, "//div[@class='services-new__item-title'][ contains(text(), 'Музыка')]")
    LANG_LINK = (By.CSS_SELECTOR, '[title="Выбрать язык"]')
    LANG_MORE_LINK = (By.CSS_SELECTOR, '[data-statlog="head.lang.more"]')


class AuthPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, 'input#passp-field-login')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input#passp-field-passwd')
    PASSWORD_ERROR = (By.CSS_SELECTOR, '[data-t="field:error-passwd"]')
    LOGIN_ERROR = (By.CSS_SELECTOR, '[data-t="field:error-login"]')
    COMMON_AUTH_ERROR = (By.CSS_SELECTOR, '.Textinput-Hint_state_error')


class YandexMailPageLocators:
    USERNAME = (By.CSS_SELECTOR, 'a.user-account>span.user-account__name')
    LOGOUT_LINK = (By.CSS_SELECTOR, "[aria-label='Выйти из аккаунта']")


class LangPageLocators:
    BUTTON_LANG_SELECT = (By.CSS_SELECTOR, '.select__button')
    LANG_SELECT = (By.CSS_SELECTOR, '[name="intl"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.form__controls> button')