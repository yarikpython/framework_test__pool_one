from selenium.webdriver.common.by import By


class BasePageLocators:
    ALERT_COOKIE = (By.CLASS_NAME, 'lg-cc lg-cc_visible')
    BUTTON_ACCEPT_COOKIE = (By.CSS_SELECTOR, 'button.lg-cc__button lg-cc__button_type_action')


class MainPageLocators:
    MAIL_LINK = (By.CSS_SELECTOR, '[data-statlog="notifications.mail.logout.title"]')
    NAV_VIDEO_LINK = (By.CSS_SELECTOR, '[data-id="video"]')
    NAV_IMAGES_LINK = (By.CSS_SELECTOR, '[data-id="images"]')
    NAV_NEWS_LINK = (By.CSS_SELECTOR, '[data-id="news"]')
    NAV_MAPS_LINK = (By.CSS_SELECTOR, '[data-id="maps"]')
    NAV_MARKET_LINK = (By.CSS_SELECTOR, '[data-id="market"]')
    NAV_TRANSLATE_LINK = (By.CSS_SELECTOR, '[data-id="translate"]')
    NAV_MUSIC_LINK = (By.CSS_SELECTOR, '[data-id="music"]')
    LANG_LINK = (By.CSS_SELECTOR, '[title="Выбрать язык"]')
    LANG_MORE_LINK = (By.CSS_SELECTOR, '[data-statlog="head.lang.more"]')


class AuthPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, 'input#passp-field-login')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input#passp-field-passwd')
    PASSWORD_ERROR = (By.CSS_SELECTOR, '[data-t="field:error-passwd"]')
    LOGIN_ERROR = (By.CSS_SELECTOR, '[data-t="field:error-login"]')


class YandexMailPageLocators:
    USERNAME = (By.CSS_SELECTOR, 'a.user-account>span.user-account__name')
    LOGOUT_LINK = (By.CSS_SELECTOR, "[aria-label='Выйти из аккаунта']")


class LangPageLocators:
    BUTTON_LANG_SELECT = (By.CSS_SELECTOR, '.select__button')
    LANG_SELECT = (By.CSS_SELECTOR, '[name="intl"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.form__controls> button')