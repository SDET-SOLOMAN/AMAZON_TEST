import time
import allure
from pages.pharmacy_page import PharmacyPage
from src.urls import Urls


@allure.epic("test verify redirection from pharmacy page to standard sign in form")
class TestPharmacyPage:
    url = Urls()

    @allure.title("Verify the standard 'sign in' form is appears after redirection from pharmacy page")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_redirect_to_sign_in_form(self, driver):
        page = PharmacyPage(driver, self.url.pharmacy_url)
        page.open()
        page.navigate_to_pharmacy(driver)
        page.check_element_is_displayed()
        value = page.check_element_is_visible()
        time.sleep(3)
        assert value is None != True, "sign_in_form is visible"
