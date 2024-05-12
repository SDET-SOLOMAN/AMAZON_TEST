from conftest import driver
from locators.pharmacy_locators import PharmacyLocators
from pages.base_page import BasePage
from src.urls import Urls


class PharmacyPage(BasePage):
    locators = PharmacyLocators
    url = Urls()

    def navigate_to_pharmacy(self, driver):
        self.element_is_visible(self.locators.SIGN_UP_SIGN_IN).click()

    def check_element_is_displayed(self):
        sign_in_form = self.element_is_visible(self.locators.SIGN_IN_FORM)
        return self.element_is_displayed(sign_in_form)

    def check_element_is_visible(self):
        pass
