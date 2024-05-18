import allure
from amazoncaptcha import AmazonCaptcha
import pytest

from locators.login_locators import LoginLocators
from locators.shopping_cart_locators import ShoppingCartLocators
from pages.shopping_cart_page import ShoppingCartPage
from src.urls import Urls
from locators.main_locators import MainLocators
@allure.epic("test shopping cart pages")
class TestShoppingCart:
    url = Urls()
    main_locators = MainLocators()
    login_locators = LoginLocators()
    shopping_cart_locators = ShoppingCartLocators()

    @allure.title("TC_005.014 | Verify that the icon shopping cart is clickable.")
    @allure.description("check shopping cart is clickable")
    def test_shopping_cart_is_clickable(self, driver, captcha):
        page = ShoppingCartPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.add_one_item_to_shopping_cart()
        expected_text = "Shopping Cart"
        actual_text = page.get_text(self.shopping_cart_locators.TITLE_SHOPPING_CART)
        with allure.step("Check result"):
            assert actual_text == expected_text
            f"Unexpected text, expected text {expected_text}, actual_text {actual_text}"

    @allure.title("TC_005.013 | Verify that the user sees the number of products on the shopping cart icon.")
    @allure.description("check counter of icon shopping cart")
    def test_check_number_items_displays_in_icon_cart(self, driver, captcha):
        page = ShoppingCartPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.add_one_item_to_shopping_cart()
        expected_result = '1'
        actual_result = page.get_text(self.login_locators.COUNTER_ITEMS_SHOPPING_CART)
        assert actual_result == expected_result
