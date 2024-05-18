import allure
import pytest
from selenium import webdriver
import locators
import locators.pharmacy_locators
from pages.pharmacy_page import PharmacyPage
from pages.base_page import BasePage
from src.urls import Urls
from locators import pharmacy_locators


@allure.epic("Test to verify Amazon Pharmacy logo presence")
class TestAmazonPharmacyLogo:
    url = Urls

    @allure.title("TC003.002.Verify Amazon Pharmacy logo is present on the UI")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_amazon_pharmacy_logo(self, driver):
        driver = webdriver.Chrome()
        page = BasePage(driver, self.url.base_url)
        page.open()
        page.navigate_to_medical_care_field()
        navigate_to_medical_care = page.element_is_visible(locators.MEDICAL_CARE_LINK)
        page.hold_mouse_on_pharm_popup_box()

        # page.select_pharmacy_field()
        # page.click_on_pharmacy_field()
        # amazon_pharmacy_logo_present = page.is_amazon_pharmacy_logo_present()
        # assert amazon_pharmacy_logo_present
        #
        # driver.quit()
