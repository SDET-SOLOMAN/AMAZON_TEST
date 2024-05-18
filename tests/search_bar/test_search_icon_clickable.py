import time

import pytest
import allure
from selenium.webdriver.chrome import webdriver

from pages.search_bar_page import SearchBarPage
from src.urls import Urls
from locators.search_bar_locators import SearchBarLocators
from pages.base_page import BasePage
from amazoncaptcha import AmazonCaptcha
# driver = webdriver.Chrome(executable_path = "driver/chromedriver")


class TestSearchBar:

    url = Urls()
    search_bar_locators = SearchBarLocators()


    def test_search_icon_is_clickable(self, driver, captcha):
        page = SearchBarPage(driver, self.url.base_url)
        page.open()
        time.sleep(10)
        page.type_in_search_bar()
        expected_title = '"flowers"'
        actual_title = page.get_text(self.search_bar_locators.TITLE_FLOWERS)
        assert actual_title == expected_title, f"Unexpected text, expected text {expected_title}, actual_text {actual_title}"
        time.sleep(5)





