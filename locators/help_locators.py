from selenium.webdriver.common.by import By



class HelpLocators():
    #captchalocators
    IMG_CAPTCHA = (By.XPATH, "//*[@class='a-row a-text-center']/img")
    CAPTCHA_FIELD = (By.CSS_SELECTOR, "#captchacharacters")
    CAPTCHA_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    #helplocators
    HELP_BOTTOM_LINK = (By.XPATH, "//a[contains(text(), 'Help')]")
    AMAZON_CUSTOMER_SERVICE_TITLE = (By.XPATH, "//h1")

    
