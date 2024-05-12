import allure
from locators.search_bar_locators import SearchBarLocators
from pages.base_page import BasePage
from src.user_data import UserData


class SearchBarPage(BasePage):
    locators = SearchBarLocators()
    user = UserData()

    def type_in_search_bar(self):
        self.element_is_visible(SearchBarLocators.SEARCH_FIELD).send_keys('flowers')
        self.element_is_visible(SearchBarLocators.SEARCH_ICON).click()

    def get_text(self, locator):
        return self.element_is_visible(locator).text
