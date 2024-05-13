

class GroceriesLocators:
    PRODUCE = ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[1]")
    MEAT_SEAFOOD = ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[2]")
    DAIRY_EGGS_CHEESE = ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[3]")
    SNACKS_PANTRY_STAPLES = ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[4]")
    BEAUTY_HEALTH_PERSONAL_CARE = \
        ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[5]")
    HOUSEHOLD_ESSENTIALS = ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[6]")
    BEVERAGES = ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[7]")
    PET_FOOD = ("xpath", "(//div[@class='bxc-grid__content   bxc-grid__content--light  celwidget'])[8]")
    SEARCH_BOX = ("css selector", "input[id='twotabsearchtextbox']")
    RESULT_TEXT = ("css selector", "span[class='a-color-state a-text-bold']")
    INPUT_ZIP_CODE = ("css selector", "input[id='alm-stores-zip-checker-input']")
    CHANGE_LOCATION = ("css selector", "input[class='a-button-input']")
    SHOPPING_OUTSIDE_TEXT = ("xpath", "//h4[contains(text(), 'Shopping outside')]")
    STORES_AVAILABLE_TEXT = ("xpath", "//h4[contains(text(), 'Shop stores available')]")
    ERROR_ZIP_CODE_MSG = ("css selector", "div[class='a-alert-content']")

