import time

import pytest
import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select

from pages.search_bar_page import SearchBarPage
from src.urls import Urls
from locators.search_bar_locators import SearchBarLocators

@allure.epic("Test Drop-down menu in the search box")
class TestSearchBar:
    url = Urls()
    drop_down_locators = SearchBarLocators()

    @pytest.mark.xfail
    @allure.title("TC_002.002 | Verify that the drop-down menu in the search box is clickable")
    @allure.severity(allure.severity_level.NORMAL)
    def test_drop_down_menu(self, driver, captcha):
        page = SearchBarPage(driver, self.url.base_url)
        with allure.step("Navigate ti the home page"):
            page.open()
        with allure.step("Click on the search field"):
            page.navigate_and_click_on_search_field()

        search_suggestions = SearchBarLocators.SELECT_ITEM_LIST
        if len(search_suggestions) >= 3:
            page.scroll_to(search_suggestions[2])
            # Click on the third option
            search_suggestions[2].click()

            new_locator = SearchBarLocators.SORT_FILTER
            assert new_locator.is_displayed(), "New locator is not visible on the page"
