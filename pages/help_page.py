import allure
import pytest
from pages.base_page import BasePage
from locators.help_locators import HelpLocators as HL
from src.urls import Urls


class HelpPage(BasePage):

    def scroll_to_help_bottom_menu(self):
        element = self.element_is_clickable(HL.HELP_BOTTOM_LINK)
        self.scroll_to(element)

    def click_on_help_bottom_menu(self):
        self.element_is_clickable(HL.HELP_BOTTOM_LINK, 5).click()

    def should_be_customer_service_page(self):
        assert self.get_text(HL.AMAZON_CUSTOMER_SERVICE_TITLE) == "Welcome to Amazon Customer Service", "This is not Customer Service Page"




