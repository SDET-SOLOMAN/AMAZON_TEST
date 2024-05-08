from pages.login_page import LoginPage
from locators.main_locators import MainLocators
from src.urls import Urls
from locators.login_locators import LoginLocators

class TestLogin:
    url = Urls()
    main_locators = MainLocators()
    login_locators = LoginLocators()

    def test_login(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        assert page.login_name() == self.login_locators.LOGIN_NAME
