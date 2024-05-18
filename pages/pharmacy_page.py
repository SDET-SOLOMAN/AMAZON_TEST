import allure
from conftest import driver
from locators.pharmacy_locators import PharmacyLocators
from pages.base_page import BasePage
from src.urls import Urls


class PharmacyPage(BasePage):
    locators = PharmacyLocators
    url = Urls()
    page = BasePage

    def navigate_to_pharmacy(self, driver):
        self.element_is_visible(self.locators.SIGN_UP_SIGN_IN).click()

    def check_element_is_displayed(self):
        sign_in_form = self.element_is_visible(self.locators.SIGN_IN_FORM)
        return self.element_is_displayed(sign_in_form)

    def check_element_is_visible(self):
        pass

    def prime_savings(self):
        self.element_is_clickable(self.locators.PRIME_SAVINGS_BOX).click()

    def check_prime_savings_is_displayed(self):
        prime_saving = self.element_is_visible(self.locators.PRIME_SAVINGS_TITLE)
        return self.element_is_displayed(prime_saving)

