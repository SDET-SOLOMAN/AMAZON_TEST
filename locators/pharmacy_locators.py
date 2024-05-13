
class PharmacyLocators:
    MEDICAL_CARE_LINK = ("xpath", "//*[@id='nav_link_allhealthingress']")
    PHARMACY_LINK = ("xpath", "//a[contains(@href, 'pharmacy')]/div/img")
    PHARMACY_LOGO = ("xpath", "//*[@id='desktop-pharmacy-logo']//div[1]")
    ONE_MEDICAL = ("xpath", "//*[@title='prime one medical']")
    SIGN_UP_SIGN_IN = ("xpath", "//*[@aria-label='Sign up']")
    SIGN_IN_FORM = ("xpath", "//*[@class='a-section a-spacing-base']")
    PRIME_SAVINGS_TITLE = ("xpath", "//*[@id='primesavings']//h3/strong")
    PRIME_SAVINGS_BOX = ("xpath", "//a[@href='pricing?ref_=sf2_primesavings_t1#primesavings']")
