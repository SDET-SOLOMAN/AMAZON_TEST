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

