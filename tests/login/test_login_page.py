import time

import allure
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
            assert page.check_sinin_page() == self.login_locators.SIN_IN_TEXT





































































    @allure.title("TC_005.006 |Verify that 'Keep Me Signed In' Checkbox modal window appears")
    @allure.description("check details link is clickable")
    def test_check_details_link(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        time.sleep(10)
        page.click_detail_link()
        actual_text = page.get_text(self.login_locators.DETAIL_TITLE_MODAL_WINDOW)
        expected_text = '"Keep Me Signed In" Checkbox'
        with allure.step("Check result"):
            assert actual_text == expected_text, f"Unexpected text, expected text {expected_text}, actual_text {actual_text}"

    @allure.title("TC_005.007 |Verify that Shop on Amazon Business link redirects to amazon business sign in")
    @allure.description("check business link is clickable")
    def test_check_business_link(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        time.sleep(10)
        page.click_business_link()
        actual_text = page.get_text(self.login_locators.SIGN_IN_BUSINESS_TITLE)
        expected_text = 'Sign in with business credentials'
        with allure.step("Check result"):
            assert actual_text == expected_text, f"Unexpected text, expected text {expected_text}, actual_text {actual_text}"

    @allure.title("TC_005.009 | Verify that when the user is trying to log in, the user cannot enter an incorrect email")
    @allure.description("check incorrect email address")
    def test_negative_email_address(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        time.sleep(10)
        page.type_invalid_email()
        actual_text = page.get_text(self.login_locators.ERROR_MESSAGE_INCORRECT_EMAIL)
        expected_text = 'There was a problem We cannot find an account with that email address'
        with allure.step("Check result"):
            assert actual_text in expected_text, f"Unexpected text, expected text {expected_text}, actual_text {actual_text}"

    @allure.title("TC_005.01 |Verify that Conditions of Use link is clickable.")
    @allure.description("check conditions of use_link is clickable")
    def test_check_conditions_of_use_link(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        time.sleep(10)
        page.click_to_conditions_of_use_link()
        with allure.step("Check result"):
            assert page.checking_title_page() == self.login_locators.TITLE_TEXT_CONDITION_PAGE

    @allure.title("TC_005.010 | Verify that the button 'continue' is clickable.")
    @allure.description("check continue button is clickable")
    def test_check_continue_btn(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        time.sleep(10)
        page.click_to_continue_btn()
        with allure.step("Check result"):
            assert page.checking_title_password_page() == self.login_locators.PASSWORD_TEXT

    @allure.title("TC_005.011 | Verify that the button 'Sign in' is clicable in modal window.")
    @allure.description("check sign in btn in modal window is clickable")
    def test_check_sign_in_btn_in_modal_window(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        time.sleep(10)
        page.click_to_sign_in_btn_in_modal_window()
        actual_text = page.get_text(self.login_locators.SIN_IN_PAGE)
        expected_text = 'Sign in'
        with allure.step("Check result"):
            assert actual_text in expected_text, f"Unexpected text, expected text {expected_text}, actual_text {actual_text}"
