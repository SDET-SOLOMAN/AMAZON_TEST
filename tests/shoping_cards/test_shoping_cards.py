import time

import allure
from amazoncaptcha import AmazonCaptcha
import pytest
from pages.main_page import MainPage
from src.urls import Urls
from locators.login_locators import LoginLocators

@allure.epic("test main page and shoping cards")
class TestLogin:
    url = Urls()

    login_locators = LoginLocators()

    @allure.title("TC_005.014 | Verify that the icon shopping cart is clickable.")
    def test_shopping_card_is_clickable(self, driver):
        page = MainPage(driver,self.url.base_url)
        page.open()
        page.login()
        time.sleep(25)
        page.click_to_first_shoping_card()







