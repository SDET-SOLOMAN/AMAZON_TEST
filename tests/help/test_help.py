import allure
import pytest
from pages.help_page import HelpPage
from src.urls import Urls
import time

@allure.title("TC_001.001")
@allure.description("Verify that clicking Help redirects to the Amazon Customer Service page")
def test_help_redirect_to_customer_service(driver, captcha):
    page = HelpPage(driver, Urls.base_url)
    page.open()
    page.scroll_to_help_bottom_menu()
    page.click_on_help_bottom_menu()
    page.should_be_customer_service_page()

@allure.title("TC_001.002")
@allure.description("Verify that -Track Your Package- is present and clickable on the Amazon Customer Service page")
def test_check_track_your_package_link(driver, captcha):
    page = HelpPage(driver, Urls.base_url)
    page.open()
    page.go_to_amazone_service_page()
    page.click_on_track_your_package_link()
    page.switch_to_second_window()
    page.should_be_track_your_package_page()

@allure.title("TC_001.003")
@allure.description("Verify that -Check the Status of Your Refund- is present and clickable on the Amazon Customer Service page")
def test_check_the_status_refund_link(driver, captcha):
    page = HelpPage(driver, Urls.base_url)
    page.open()
    page.go_to_amazone_service_page()
    page.click_on_check_status_of_refund_link()
    page.switch_to_second_window()
    page.should_be_check_status_of_refund_page()

@allure.title("TC_001.004")
@allure.description("Verify that -Your Account - is present and clickable in the 'Let Us Help You' menu at the bottom of Amazon main page")
def test_check_your_account_link(driver, captcha):
    page = HelpPage(driver, Urls.base_url)
    page.open()
    page.click_on_your_account_link()
    page.should_be_your_account_page()

@allure.title("TC_001.005")
@allure.description("Verify that -Help- link is present and clickable on the 'Sing in' page")
def test_check_help_at_sign_in_page(driver, captcha):
    page = HelpPage(driver, Urls.base_url)
    page.open()
    page.click_on_sign_in_link()
    page.should_be_sign_in_page()
    page.click_on_sign_in_page_help_link()
    page.switch_to_second_window()
    page.should_be_customer_service_page()
