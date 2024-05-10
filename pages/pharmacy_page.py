import allure
from locators.pharmacy_locators import PharmacyLocators
from pages.base_page import BasePage
from src.user_data import UserData


class LoginPage(BasePage):
    locators = PharmacyLocators()
    user = UserData()