import pytest
import allure
from src.groceries_data import GroceriesData
from pages.groceries_page import GroceriesPage
from locators.groceries_locators import GroceriesLocators
from src.urls import Urls


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

    @allure.title("Verify that the entered zip code is displayed in the Available Stores section of the Groceries page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_displaying_zip_code_on_available_stores_section(self, driver):
        page = GroceriesPage(driver, self.url.groceries_url)

        with allure.step("Navigate to the groceries page"):
            page.open()
        with allure.step("Enter the zip code - 10002 in the input field"):
            page.type_zip_code(self.data.zip_code)
        with allure.step("Click on 'Change location' button"):
            page.element_is_clickable(self.locators.CHANGE_LOCATION).click()

        page.text_is_present(self.locators.SHOPPING_OUTSIDE_TEXT, self.data.zip_code)

        assert page.is_zip_code_displayed(self.data.zip_code)

    @pytest.mark.parametrize("zip_codes", data.zip_codes)
    def test_verify_error_message_if_postal_code_less_than_six_digit(self, driver, zip_codes):
        page = GroceriesPage(driver, self.url.groceries_url)
        page.open()

        page.type_zip_code(zip_codes)
        page.element_is_clickable(self.locators.CHANGE_LOCATION).click()
        error_msg = page.element_is_visible(self.locators.ERROR_ZIP_CODE_MSG).text

        assert "Please enter a valid zip code" == error_msg


