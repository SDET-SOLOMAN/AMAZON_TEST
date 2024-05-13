import pytest
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha
from locators.help_locators import HelpLocators as HL


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def captcha(driver):
    driver.get('https://www.amazon.com/')
    link = driver.find_element(*HL.IMG_CAPTCHA).get_attribute("src")
    image = AmazonCaptcha.fromlink(link)
    captcha_value = AmazonCaptcha.solve(image)
    driver.find_element(*HL.CAPTCHA_FIELD).send_keys(captcha_value)
    driver.find_element(*HL.CAPTCHA_BUTTON).click()
    yield


