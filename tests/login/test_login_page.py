import time

import allure
from amazoncaptcha import AmazonCaptcha
import pytest
from pages.login_page import LoginPage
from locators.main_locators import MainLocators
from src.urls import Urls
from locators.login_locators import LoginLocators

@allure.epic("test login and logout pages")
class TestLogin:
    url = Urls()
    main_locators = MainLocators()
    login_locators = LoginLocators()

    @allure.title("test login")
    @allure.description("check login")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_login(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        with allure.step("Check result"):
           assert page.login_name() == self.login_locators.LOGIN_NAME

    @allure.title("test logout")
    @allure.description("check logout")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.xfail(reason="Site authorization is not always stable")
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_logout(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.hold_mouse_to_account()
        page.clik_to_logout()
        with allure.step("Check result"):
            assert page.check_signin_page() == self.login_locators.SIN_IN_TEXT

    @allure.title("test modal window sign in")
    @allure.description("check modal window sign in")
    def test_check_the_modal_window(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        # time.sleep(10)
        page.hold_mouse_to_account()
        modal_window = page.check_modal_window_sign_in_is_displayed()
        with allure.step("Check result"):
            assert modal_window is True, 'Modal window Sign in appeared'

    @allure.title("test option forgot password")
    @allure.description("check option forgot password")
    def test_check_option_forgot_password(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        # time.sleep(10)
        page.click_forgot_password_link()
        expected_text = "Password assistance"
        actual_text = page.get_text(self.login_locators.PASSWORD_ASSISTANCE)
        with allure.step("Check result"):
            assert actual_text == expected_text, f"Unexpected text, expected text {expected_text}, actual_text {actual_text}"

    @allure.title("test need help link")
    @allure.description("check need help link is clickable")
    def test_check_need_help_link(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        # time.sleep(10)
        page.click_need_help_link()
        with allure.step("Check result"):
            assert page.check_need_help_drop_down() == self.login_locators.DROP_DOWN_NEED_HELP

    @allure.title("test change email or phone number")
    @allure.description("check option change password or phone number")
    def test_change_the_email(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        # time.sleep(10)
        email_field = page.change_the_email()
        with allure.step("Check result"):
            assert email_field is True, 'User can type new email or phone number'

    @allure.title("test email error message")
    @allure.description("checking email error message")
    def test_check_email_error_message(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        # time.sleep(10)
        page.click_to_continue_button_with_empty_email()
        expected_text = "Enter your email or mobile phone number"
        actual_text = page.get_text(self.login_locators.ERROR_MESSAGE_EMPTY_EMAIL)
        with allure.step("Check result"):
            assert actual_text == expected_text
            f"Unexpected text, expected text {expected_text}, actual_text {actual_text}"

    @allure.title("test privacy notice link")
    @allure.description("check privacy notice link is clickable")
    def test_check_privacy_notice_link_is_clickable(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        # time.sleep(10)
        page.click_privacy_notice_link()
        with allure.step("Check result"):
            assert page.check_privacy_notice_page() == self.login_locators.PRIVACY_NOTICE_TEXT


