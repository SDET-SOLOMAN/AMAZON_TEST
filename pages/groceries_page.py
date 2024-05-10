from pages.base_page import BasePage
from locators.groceries_locators import GroceriesLocators
from selenium.common.exceptions import TimeoutException


def peel_text(text, symbol):
    return text.strip(symbol)


class GroceriesPage(BasePage):

    locators = GroceriesLocators

    def click_on_product_card(self, locator):
        self.element_is_clickable(locator).click()

    def is_right_product_catalog(self, product_name):
        try:
            actual_search_box_text = peel_text(self.element_is_visible(self.locators.SEARCH_BOX).get_attribute('value'),
                                               '"')
            actual_result_text = peel_text(self.element_is_visible(self.locators.RESULT_TEXT).text, '"')
            expected_text = product_name

            return actual_result_text == expected_text and actual_search_box_text == expected_text
        except TimeoutException:
            return False


