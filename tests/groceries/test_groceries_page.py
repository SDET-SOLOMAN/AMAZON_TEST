import pytest
import allure
from src.groceries_data import GroceriesData
from pages.groceries_page import GroceriesPage
from src.urls import Urls


@allure.epic("Test groceries page")
class TestGroceries:

    url = Urls()
    data = GroceriesData()

    @pytest.mark.parametrize("products", data.product_cards)
    @allure.title("Verify that after clicking on the product card, the catalog page with the selected product appears")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_navigation_of_product_cards(self, driver, products):
        page = GroceriesPage(driver, self.url.groceries_url)
        with allure.step("Navigate to the groceries page"):
            page.open()
        with allure.step("Click on each the product card in the group"):
            page.click_on_product_card(products[0])

        assert page.is_right_product_catalog(products[1])
