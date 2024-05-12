from pages.base_page import BasePage
from locators.groceries_locators import GroceriesLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


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

    def is_zip_code_displayed(self, zipcode):
        shopping_outside_text = self.element_is_visible(self.locators.SHOPPING_OUTSIDE_TEXT).text
        stores_available_header = self.element_is_visible(self.locators.STORES_AVAILABLE_TEXT).text

        return zipcode in shopping_outside_text and zipcode in stores_available_header

    def type_zip_code(self, zipcode):
        input_box = self.element_is_visible(self.locators.INPUT_ZIP_CODE)
        input_box.send_keys(zipcode)

    def text_is_present(self, locator, text):
        wait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, text))
