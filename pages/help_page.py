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

    def go_to_amazone_service_page(self):
        self.click_on_help_bottom_menu()

    def click_on_track_your_package_link(self):
        self.element_is_clickable(HL.TRACK_YOUR_PACKAGE_LINK, 5).click()

    def click_on_check_status_of_refund_link(self):
        self.element_is_clickable(HL.CHECK_STATUS_OF_REFUND, 5).click()

    def click_on_your_account_link(self):
        self.element_is_clickable(HL.YOUR_ACCOUNT_LINK, 5).click()

    def click_on_sign_in_link(self):
        self.element_is_clickable(HL.SIGN_IN_LINK, 5).click()

    def click_on_sign_in_page_help_link(self):
        self.element_is_clickable(HL.SIGN_IN_PAGE_HELP_LINK, 5).click()

    def should_be_track_your_package_page(self):
        assert self.get_text(HL.TRACK_YOUR_PACKAGE_TITLE) == "Track Your Package", "This is not Track Your Package Page"

    def should_be_check_status_of_refund_page(self):
        assert self.get_text(HL.CHECK_STATUS_OF_REFUND_TITLE) == "Check the Status of Your Refund", "This is not Check the Status of Your Refund Page"

    def should_be_your_account_page(self):
        assert self.get_text(HL.YOUR_ACCOUNT_PAGE_TITLE) == "Your Account", "This is not Your Account Page"

    def should_be_sign_in_page(self):
        assert self.get_text(HL.SIGN_IN_PAGE_TITLE) == "Sign in", "This is not Sign in"

    def switch_to_second_window(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])



