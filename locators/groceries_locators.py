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


