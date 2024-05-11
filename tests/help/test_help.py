import allure
import pytest
from pages.help_page import HelpPage
from src.urls import Urls

@allure.title("TC_001.001")
@allure.description("Verify that clicking Help redirects to the Amazon Customer Service page")
def test_help_redirect_to_customer_service(driver, captcha):
    page = HelpPage(driver, Urls.base_url)
    page.open()
    page.scroll_to_help_bottom_menu()
    page.click_on_help_bottom_menu()
    page.should_be_customer_service_page()
