from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData
import allure


class ShoppingCartPage(BasePage):
    locators = LoginLocators()
    user = UserData()

    def get_text(self, locator):
        with allure.step('Find text'):
            return self.element_is_visible(locator).text

    def add_one_item_to_shopping_cart(self):
        with allure.step('Click to item'):
            self.element_is_visible(self.locators.FIRST_LIST_ITEMS_MAIN_PAGE).click()
        with allure.step("Click to the button 'Add to Cart'"):
            self.element_is_visible(self.locators.ADD_TO_CART_BTN).click()
        with allure.step('Click to icon shopping cart'):
            self.element_is_visible(self.locators.SHOPPING_CART).click()



