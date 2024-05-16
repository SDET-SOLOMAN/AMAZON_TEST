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
        page = GroceriesPage(driver, self.url.base_url)
        page1 = GroceriesPage(driver, self.url.groceries_url)
        with allure.step("Open Amazon page"):
            page.open()
        with allure.step("Navigate to the groceries page"):
            page1.open()
        with allure.step("Enter the zip code - 10002 in the input field"):
            page.type_zip_code(self.data.zip_code)
        with allure.step("Click on 'Change location' button"):
            page.element_is_clickable(self.locators.CHANGE_LOCATION).click()
        with allure.step("Check search text is present"):
            page.text_is_present()
        with allure.step("Assert zip code is correct"):
            assert page.is_zip_code_displayed(self.data.zip_code)

    @pytest.mark.parametrize("zip_codes", data.zip_codes)
    @allure.title("Verify that an error message appears after entering a postal code that is greater and less than 5 digits")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_that_error_msg_is_displayed_after_entering_invalid_zip_code(self, driver, zip_codes):
        page = GroceriesPage(driver, self.url.groceries_url)

        with allure.step("Navigate to the groceries page"):
            page.open()
        with allure.step("Enter the zip codes that less and greater than 5 digits"):
            page.type_zip_code(zip_codes)
        with allure.step("Click on 'Change location' button"):
            page.element_is_clickable(self.locators.CHANGE_LOCATION).click()

        assert page.is_zip_code_error_msg_displayed(self.data.zip_code_error_msg)


