import time
import allure
import pytest
from pages.pharmacy_page import PharmacyPage
from src.urls import Urls


@allure.epic("test verify redirection from pharmacy page to prime savings")
class TestPharmacyPage:
    url = Urls()

    @allure.title("Verify Prime savings at Amazon Pharmacy is present after redirection from pharmacy page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_prime_saving_title(self, driver):
        page = PharmacyPage(driver, self.url.pharmacy_url)
        page.open()
        page.prime_savings()
        prime_saving = page.element_is_visible(page.locators.PRIME_SAVINGS_TITLE)
        time.sleep(3)
        assert page.element_is_displayed(prime_saving)

