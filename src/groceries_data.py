from locators.groceries_locators import GroceriesLocators


class GroceriesData:
    locators = GroceriesLocators()
    zip_code = "10002"

    product_cards = [
        [locators.PRODUCE, 'produce'],
        [locators.MEAT_SEAFOOD, 'meat and seafood'],
        [locators.DAIRY_EGGS_CHEESE, 'dairy, cheese & eggs'],
        [locators.SNACKS_PANTRY_STAPLES, 'snacks'],
        [locators.BEAUTY_HEALTH_PERSONAL_CARE, 'beauty, health and personal care'],
        [locators.HOUSEHOLD_ESSENTIALS, 'household essentials'],
        [locators.BEVERAGES, 'beverages'],
        [locators.PET_FOOD, 'pet food']
    ]

