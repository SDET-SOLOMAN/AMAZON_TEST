import allure
from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData
from amazoncaptcha import AmazonCaptcha


class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()

    def login_name(self):
        with allure.step("Find text Log_in"):
            name_text = self.element_is_visible(self.locators.LOG_IN_TEXT)
        return name_text.text

    def hold_mouse_to_account(self):
        with allure.step("Hold a mouse on login menu'"):
            self.hold_mouse_on_element(self.element_is_clickable(self.locators.ACCOUNT_LINK))

    def clik_to_logout(self):
        with allure.step("Click to sign_out menu "):
            self.element_is_clickable(self.locators.SIN_OUT).click()

    def check_signin_page(self):
        with allure.step("Find text: sign_in"):
            page_name = self.element_is_visible(self.locators.SIN_IN_PAGE)
        return page_name.text

    def check_modal_window_sign_in_is_displayed(self):
        with allure.step("Find modal window 'sign_in' "):
            modal_window = self.element_is_visible(self.locators.MODAL_WINDOW_SIGN_IN)
        return self.element_is_displayed(modal_window)


    def click_detail_link(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(LoginLocators.ACCOUNT_LINK).click()
        with allure.step("Enter email"):
            self.element_is_visible(self.locators.EMAIL_OR_PHONE_FIELD).send_keys(self.user.email)
        with allure.step("Click to continue btn"):
            self.element_is_visible(self.locators.CONTINUE_BTN).click()
        with allure.step("Click to details link"):
            self.element_is_visible(self.locators.LINK_DETAILS).click()

    def get_text(self, locator):
        with allure.step("Find the text"):
            return self.element_is_visible(locator).text

    def click_business_link(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(LoginLocators.ACCOUNT_LINK).click()
        with allure.step("Click to link shop on amazon business"):
            self.element_is_visible(self.locators.LINK_SHOP_ON_AMAZON_BUSINESS).click()

    def type_invalid_email(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(LoginLocators.ACCOUNT_LINK).click()
        with allure.step("Enter email address"):
            self.element_is_visible(self.locators.EMAIL_OR_PHONE_FIELD).send_keys(self.user.incorrect_email)
        with allure.step("Click to continue button"):
            self.element_is_visible(self.locators.CONTINUE_BTN).click()

    def click_to_conditions_of_use_link(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(LoginLocators.ACCOUNT_LINK).click()
        with allure.step("Click to condition of use link"):
            self.element_is_visible(self.locators.CONDITIONS_OF_USE).click()

    def checking_title_page(self):
        with allure.step("Find the text: Condition of use"):
            title_text = self.element_is_visible(self.locators.TITLE_CONDITION_OF_USE)
        return title_text.text

    def click_to_continue_btn(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(LoginLocators.ACCOUNT_LINK).click()
        with allure.step("Enter email address"):
            self.element_is_visible(self.locators.EMAIL_OR_PHONE_FIELD).send_keys(self.user.email)
        with allure.step("Click to continue button"):
            self.element_is_visible(self.locators.CONTINUE_BTN).click()

    def checking_title_password_page(self):
        with allure.step("Find the text: Password"):
            text = self.element_is_visible(self.locators.PASSWORD_PAGE)
        return text.text

    def click_to_sign_in_btn_in_modal_window(self):
        with allure.step("Hold a mouse on login menu"):
            self.hold_mouse_on_element(self.locators.ACCOUNT_LINK)
        with allure.step("Click to Sign in button"):
            self.element_is_visible(self.locators.SIGN_IN_BTN_IN_MODAL_WINDOW).click()

    def click_forgot_password_link(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(self.locators.ACCOUNT_LINK).click()
        with allure.step('Enter email'):
            self.element_is_visible(self.locators.EMAIL_OR_PHONE_FIELD).send_keys(self.user.email)
        with allure.step('Click to continue button'):
            self.element_is_visible(self.locators.CONTINUE_BTN).click()
        with allure.step('Click to link forgot password'):
            self.element_is_visible(self.locators.LINK_FORGOT_PASSWORD).click()


    def password_assistance_title(self):
        with allure.step('Find text "Password assistance"'):
            name_text = self.element_is_visible(self.locators.PASSWORD_ASSISTANCE)
        return name_text.text

    def click_need_help_link(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(self.locators.ACCOUNT_LINK).click()
        with allure.step('Click to link "Need help"'):
            self.element_is_visible(self.locators.NEED_HELP).click()

    def check_need_help_drop_down(self):
        with allure.step('Find text: "forgot password", "other issue with sign in"'):
            drop_down_1 = self.element_is_present(self.locators.DROP_DOWN_FORGOT_PASSWORD).text
            drop_down_2 = self.element_is_present(self.locators.DROP_DOWN_OTHER_ISSUES_WITH_SIGN_IN).text
        return drop_down_1, drop_down_2

    def change_the_email(self):
        with allure.step("Click to login menu"):
            self.element_is_visible(self.locators.ACCOUNT_LINK).click()
        with allure.step("Enter email or phone number"):
            self.element_is_visible(self.locators.EMAIL_OR_PHONE_FIELD).send_keys(self.user.email)
        with allure.step('Click to continue button'):
            self.element_is_visible(self.locators.CONTINUE_BTN).click()
        with allure.step('Click to link change'):
            self.element_is_visible(self.locators.LINK_CHANGE).click()
        with allure.step('Find email field'):
            email_field = self.element_is_visible(self.locators.EMAIL_OR_PHONE_FIELD)
        return self.element_is_displayed(email_field)

    def click_to_continue_button_with_empty_email(self):
        with allure.step('Click to login menu'):
            self.element_is_visible(self.locators.ACCOUNT_LINK).click()
        with allure.step('Click to continue button'):
            self.element_is_clickable(self.locators.CONTINUE_BTN).click()

    def click_privacy_notice_link(self):
        with allure.step('Click to login menu'):
            self.element_is_visible(self.locators.ACCOUNT_LINK).click()
        with allure.step('Click to "privacy notice" link'):
            self.element_is_visible(self.locators.PRIVACY_NOTICE).click()

    def check_privacy_notice_page(self):
        with allure.step('Find text:"Privacy notice"'):
            page_name = self.element_is_visible(self.locators.PRIVACY_NOTICE_PAGE)
            print(page_name.text)
        return page_name.text



