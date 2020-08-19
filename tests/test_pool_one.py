import allure
from allure_commons.types import AttachmentType
from pages.locators import AuthPageLocators
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.yandex_mail_page import YandexMailPage
from pages.lang_page import LangPage


@allure.feature('Yandex Mail Auth')
@allure.story('Login Correct Username Password')
def test_mail_correct_user(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_mail()
    mail_window = driver.window_handles[1]
    driver.switch_to.window(mail_window)
    auth_page = AuthPage(driver, driver.current_url)
    auth_page.send_username('AutotestUser')
    auth_page.send_password('AutotestUser123')
    yandex_mail_page = YandexMailPage(driver, driver.current_url)
    username = yandex_mail_page.get_username()
    with allure.step('Screenshot'):
        allure.attach(driver.get_screenshot_as_png(), name='screenshot username', attachment_type=AttachmentType.PNG)
    assert username == 'AutotestUser'


@allure.feature('Yandex Mail Auth')
@allure.story('Logout')
def test_logout(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_mail()
    mail_window = driver.window_handles[1]
    driver.switch_to.window(mail_window)
    auth_page = AuthPage(driver, driver.current_url)
    auth_page.send_username('AutotestUser')
    auth_page.send_password('AutotestUser123')
    yandex_mail_page = YandexMailPage(driver, driver.current_url)
    username = yandex_mail_page.get_username()
    assert username == 'AutotestUser'
    yandex_mail_page.logout()
    auth_page_after_logout = AuthPage(driver, driver.current_url)
    assert auth_page_after_logout.is_element_present(*AuthPageLocators.INPUT_PASSWORD)


@allure.feature('Yandex Mail Auth')
@allure.story('Invalid password')
def test_invalid_password(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_mail()
    mail_window = driver.window_handles[1]
    driver.switch_to.window(mail_window)
    auth_page = AuthPage(driver, driver.current_url)
    auth_page.send_username('AutotestUser')
    auth_page.send_password('NoAutotestUser123')
    with allure.step('Screenshot'):
        allure.attach(driver.get_screenshot_as_png(), name='screenshot username', attachment_type=AttachmentType.PNG)
    assert auth_page.is_element_present(*AuthPageLocators.PASSWORD_ERROR)


@allure.feature('Yandex Mail Auth')
@allure.story('Invalid username')
def test_invalid_login(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_mail()
    mail_window = driver.window_handles[1]
    driver.switch_to.window(mail_window)
    auth_page = AuthPage(driver, driver.current_url)
    auth_page.send_username('NoAutotestUser')
    with allure.step('Screenshot'):
        allure.attach(driver.get_screenshot_as_png(), name='screenshot username', attachment_type=AttachmentType.PNG)
    assert auth_page.is_element_present(*AuthPageLocators.LOGIN_ERROR)


@allure.feature("Yandex Main Links")
def test_nav_links(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_window = driver.window_handles[0]

    main_page.go_to_video()
    video_window = driver.window_handles[1]
    driver.switch_to.window(video_window)
    assert 'video' in driver.current_url
    main_page.driver.close()
    driver.switch_to.window(main_window)

    main_page.go_to_images()
    image_window = driver.window_handles[1]
    driver.switch_to.window(image_window)
    assert 'images' in driver.current_url
    main_page.driver.close()
    driver.switch_to.window(main_window)

    main_page.go_to_news()
    news_window = driver.window_handles[1]
    driver.switch_to.window(news_window)
    assert 'news' in driver.current_url
    main_page.driver.close()
    driver.switch_to.window(main_window)

    main_page.go_to_maps()
    maps_window = driver.window_handles[1]
    driver.switch_to.window(maps_window)
    assert 'maps' in driver.current_url
    main_page.driver.close()
    driver.switch_to.window(main_window)

    main_page.go_to_market()
    market_window = driver.window_handles[1]
    driver.switch_to.window(market_window)
    assert 'market' in driver.current_url
    main_page.driver.close()
    driver.switch_to.window(main_window)

    main_page.go_to_translate()
    translate_window = driver.window_handles[1]
    driver.switch_to.window(translate_window)
    assert 'translate' in driver.current_url
    main_page.driver.close()
    driver.switch_to.window(main_window)

    main_page.go_to_music()
    music_window = driver.window_handles[1]
    driver.switch_to.window(music_window)
    assert 'music' in driver.current_url
    main_page.driver.close()
    driver.switch_to.window(main_window)


@allure.feature('Yandex Change Language')
def test_change_lang(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_lang_page()
    lang_page = LangPage(driver, driver.current_url)
    lang_page.choice_lang_en()
    lang_page.save_changes()
    main_page.go_to_lang_page()
    assert main_page.get_lang() == 'en'
