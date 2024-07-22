from pages.base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):

    def click_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def get_item_added_to_basket_message(self):
        div = self.browser.find_element(*ItemPageLocators.ITEM_ADDED_BASKET_MESSAGE)
        return div.text

    def get_item_price(self):
        return self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text

    def get_item_name(self):
        return self.browser.find_element(*ItemPageLocators.ITEM_NAME).text
