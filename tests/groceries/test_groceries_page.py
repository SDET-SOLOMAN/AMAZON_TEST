import time

import pytest
import allure
from src.groceries_data import GroceriesData
from pages.groceries_page import GroceriesPage
from locators.groceries_locators import GroceriesLocators
from src.urls import Urls
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Test groceries page")
class TestGroceries:
    locators = GroceriesLocators()
    url = Urls()
    data = GroceriesData()

    @pytest.mark.parametrize("products", data.product_cards)
    @pytest.mark.xfail
    @allure.title("Verify that after clicking on the product card, the catalog page with the selected product appears")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_navigation_of_product_cards(self, driver, products):
        page = GroceriesPage(driver, self.url.groceries_url)
        with allure.step("Navigate to the groceries page"):
            page.open()
        with allure.step("Click on each the product card in the group"):
            page.click_on_product_card(products[0])

        assert page.is_right_product_catalog(products[1])

    @pytest.mark.smoke
    def test_verify_displaying_zip_code_on_available_stores_section(self, driver):
        page = GroceriesPage(driver, self.url.groceries_url)
        page.open()
        input_box = page.element_is_visible(self.locators.INPUT_ZIP_CODE)
        input_box.send_keys(self.data.zip_code)
        time.sleep(4)
        page.element_is_clickable(self.locators.CHANGE_LOCATION).click()

        wait(driver, 10).until(EC.text_to_be_present_in_element(self.locators.SHOPPING_OUTSIDE_TEXT, self.data.zip_code))

        shopping_outside_text = page.element_is_visible(self.locators.SHOPPING_OUTSIDE_TEXT).text
        stores_available_header = page.element_is_visible(self.locators.STORES_AVAILABLE_TEXT).text

        assert "10001" in shopping_outside_text
        assert "10001" in stores_available_header
