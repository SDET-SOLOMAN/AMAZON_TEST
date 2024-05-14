from selenium.webdriver.common.by import By



class HelpLocators():
    #captcha locators
    IMG_CAPTCHA = (By.XPATH, "//*[@class='a-row a-text-center']/img")
    CAPTCHA_FIELD = (By.CSS_SELECTOR, "#captchacharacters")
    CAPTCHA_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    #help locators
    HELP_BOTTOM_LINK = (By.XPATH, "//a[contains(text(), 'Help')]")
    AMAZON_CUSTOMER_SERVICE_TITLE = (By.XPATH, "//h1")
    YOUR_ACCOUNT_LINK = (By.XPATH, "//a[text()='Your Account']")
    YOUR_ACCOUNT_PAGE_TITLE = (By.XPATH, "//h1")

    #service page locators
    TRACK_YOUR_PACKAGE_LINK = (By.XPATH, "//div[@class='article-wrapper active']//div[text()='Track your package']")
    TRACK_YOUR_PACKAGE_TITLE = (By.XPATH, "//h1")
    CHECK_STATUS_OF_REFUND = (By.XPATH, "//div[text()='Check status of a refund']")
    CHECK_STATUS_OF_REFUND_TITLE = (By.XPATH, "//h1")

    #sign in page
    SIGN_IN_LINK = (By.XPATH, "//a[@id='nav-link-accountList']")
    SIGN_IN_PAGE_TITLE = (By.XPATH, "//h1")
    SIGN_IN_PAGE_HELP_LINK = (By.XPATH, "//a[@href= '/help']")
    
