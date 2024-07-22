from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def get_basket_total(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_TOTAL).text

    def get_basket_item_names(self):
        items = self.browser.find_elements(*BasketPageLocators.ITEM_NAMES)
        item_names = []
        for item in items:
            item_names.append(item.text)

        return item_names
