import allure
from locators.groceries_locators import GroceriesLocators
from pages.base_page import BasePage
from src.user_data import UserData


class GroceriesPage(BasePage):
    locators = GroceriesLocators()
    user = UserData()