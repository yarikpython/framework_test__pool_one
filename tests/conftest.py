import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import config

path_firefox_exe = os.path.normpath(config.GECKODRIVER_EXE)
path_chrome_exe = os.path.normpath(config.CHROMEDRIVER_EXE)


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    # chrome_options.headless = True
    driver = webdriver.Chrome(executable_path=path_chrome_exe, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

