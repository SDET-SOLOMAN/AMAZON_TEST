import pytest
from src.groceries_data import GroceriesData
from pages.groceries_page import GroceriesPage
from src.urls import Urls


class TestGroceries:

    url = Urls()
    data = GroceriesData()

    @pytest.mark.parametrize("products", data.product_cards)
    def test_verify_navigation_of_product_cards(self, driver, products):
        page = GroceriesPage(driver, self.url.groceries_url)
        page.open()
        page.click_on_product_card(products[0])

        assert page.is_right_product_catalog(products[1])
