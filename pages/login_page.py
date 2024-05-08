from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData


class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()

    def login_name(self):
        name_text = self.element_is_visible(self.locators.LOG_IN_TEXT)
        return name_text.text
