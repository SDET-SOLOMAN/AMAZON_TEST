

class LoginLocators:
    ACCOUNT_LINK = ("css selector", "a#nav-link-accountList")
    EMAIL_OR_PHONE_FIELD = ("css selector", "input#ap_email")
    CONTINUE_BTN = ("css selector", "input#continue")
    PASSWORD_FILD = ("css selector", "input#ap_password")
    SIGNIN_BTN = ("css selector", "input#signInSubmit")
    NOT_NOW_LINK = ("css selector", "a#ap-account-fixup-phone-skip-link")
    LOG_IN_TEXT = ("css selector", "span#nav-link-accountList-nav-line-1")
    LOGIN_NAME = "Hello, Red"
    SIN_IN_TEXT = "Sign in"
    CONDITIONS_OF_USE = ("xpath", "//div[@id='legalTextRow']/a[contains(text(), 'Conditions of Use')]")
    PRIVACY_NOTICE = ("xpath", "//div[@id='legalTextRow']/a[contains(text(), 'Privacy Notice')]")
    NEED_HELP = ("css selector", "span.a-expander-prompt")
    SIN_OUT = ("css selector", "a#nav-item-signout")
    SIN_IN_PAGE = ("css selector", "h1.a-spacing-small")
    LINK_DETAILS = ("css selector", 'a#remember_me_learn_more_link')
    LINK_SHOP_ON_AMAZON_BUSINESS = ("xpath", '//*[contains(text(), "Shop on Amazon Business")]')
    DETAIL_TITLE_MODAL_WINDOW = ("xpath", "//h4[text()='\"Keep Me Signed In\" Checkbox']")
    SIGN_IN_BUSINESS_TITLE = ("css selector", '.a-box .a-spacing-small')
    ERROR_MESSAGE_INCORRECT_EMAIL = ("xpath", "//*[contains(text(), 'We cannot find an account with that email address')]")
    TITLE_CONDITION_OF_USE = ("xpath", "//h1[contains(text(), 'Conditions of Use')]")
    TITLE_TEXT_CONDITION_PAGE = 'Conditions of Use'
    PASSWORD_PAGE = ("xpath", "//*[contains(text(), 'Password')]")
    PASSWORD_TEXT = 'Password'
    SIGN_IN_BTN_IN_MODAL_WINDOW = ("xpath", '//*[text()="Sign in"]')
    PRIVACY_NOTICE = ("css selector", "a[href*='notification_privacy_notice']")
    NEED_HELP = ("css selector", "span.a-expander-prompt")
    SIN_OUT = ("css selector", "a#nav-item-signout")
    SIN_IN_PAGE = ("css selector", "h1.a-spacing-small")
    MODAL_WINDOW_SIGN_IN = ("css selector", "div#nav-flyout-accountList")
    LINK_FORGOT_PASSWORD = ("css selector", 'a#auth-fpp-link-bottom')
    PASSWORD_ASSISTANCE = ("xpath", "//h1")
    DROP_DOWN_FORGOT_PASSWORD = ("css selector", "a#auth-fpp-link-bottom")
    DROP_DOWN_OTHER_ISSUES_WITH_SIGN_IN = ("css selector", "a#ap-other-signin-issues-link")
    DROP_DOWN_NEED_HELP = 'Forgot your password?', 'Other issues with Sign-In'
    LINK_CHANGE = ("css selector", '#ap_change_login_claim')
    ERROR_MESSAGE_EMPTY_EMAIL = ("xpath", '//*[contains(text(), "Enter your email or mobile phone number")]')
    PRIVACY_NOTICE_PAGE = ("xpath", "//h1[text()='Amazon.com Privacy Notice'] ")
    PRIVACY_NOTICE_TEXT = 'Amazon.com Privacy Notice'
    shoping_card_locators = ("css selector", "div[data-csa-c-item-id='amzn1.asin.B0CV244FWB']")


