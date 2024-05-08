from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from src.user_data import UserData
from locators.login_locators import LoginLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    timeout = 10
    locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self):
        self.element_is_visible(LoginLocators.ACCOUNT_LINK).click()
        self.element_is_visible(self.locators.EMAIL_OR_PHONE_FIELD).send_keys(self.user.email)
        self.element_is_visible(self.locators.CONTINUE_BTN).click()
        self.element_is_visible(self.locators.PASSWORD_FILD).send_keys(self.user.password)
        self.element_is_visible(self.locators.SIGNIN_BTN).click()
        # self.element_is_visible(self.locators.NOT_NOW_LINK).click()

    def open(self):
        self.driver.get(self.url)

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_not_present(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_displayed(self, element):
        return element.is_displayed()

    def hold_mouse_on_element(self, locator):
        ActionChains(self.driver).move_to_element(self.element_is_clickable(locator)).perform()

    def find_element(self,locator):
        return self.driver.find_element(locator)



