from selenium.webdriver.common.by import By

class LoginLocators:
    ACCOUNT_LINK = ("css selector", "a#nav-link-accountList")
    EMAIL_OR_PHONE_FIELD = ("css selector", "input#ap_email")
    CONTINUE_BTN = ("css selector", "input#continue")
    PASSWORD_FILD = ("css selector", "input#ap_password")
    SIGNIN_BTN = ("css selector", "input#signInSubmit")
    NOT_NOW_LINK = ("css selector", "a#ap-account-fixup-phone-skip-link")
    LOG_IN_TEXT = ("css selector", "span#nav-link-accountList-nav-line-1")
    LOGIN_NAME = "Hello, Red"
