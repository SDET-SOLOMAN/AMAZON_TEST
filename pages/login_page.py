import allure
from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData


class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()

    def login_name(self):
        with allure.step("Find text Log_in"):
            name_text = self.element_is_visible(self.locators.LOG_IN_TEXT)
        return name_text.text

    def hold_mouse_to_account(self):
        with allure.step("Hold a mouse on login menu'"):
            self.hold_mouse_on_element(self.element_is_clickable(self.locators.ACCOUNT_LINK))

    def clik_to_logout(self):
        with allure.step("Click to sign_out menu "):
            self.element_is_clickable(self.locators.SIN_OUT).click()

    def check_sinin_page(self):
        with allure.step("Find text: sign_in"):
            page_name = self.element_is_visible(self.locators.SIN_IN_PAGE)
        return page_name.text


