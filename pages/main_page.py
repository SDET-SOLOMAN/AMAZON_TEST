import time

import allure
from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData


class MainPage(BasePage):
    locators = LoginLocators()
    user = UserData()

    def click_to_first_shoping_card(self):
        with allure.step("Click on first shoping card item"):
            self.element_is_clickable(self.locators.shoping_card_locators).click()
            time.sleep(8)
