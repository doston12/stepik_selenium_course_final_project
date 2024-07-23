import time

import pytest

from pages.basket_page import BasketPage
from pages.item_page import ItemPage
from pages.locators import BasketPageLocators
from pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "MyPassword56"
        register_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

        login_page = LoginPage(browser, register_link)
        login_page.open()

        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.xfail(reason="sample test to practice setup fixture")
    def test_user_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ItemPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    @pytest.mark.xfail(reason="fails because user is already logged in, there won't be login button")
    def test_user_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ItemPage(browser, link)
        page.open()

        page.go_to_login_page()
        assert "login" in page.browser.current_url, "Login page opened"

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ItemPage(browser, link)
        page.open()

        item_name = page.get_item_name()

        page.click_add_to_basket()

        added_to_basket_msg = page.get_item_added_to_basket_message()
        assert f"{item_name} has been added to your basket." == added_to_basket_msg, ("Basked added message shows item "
                                                                                      "name correctly")


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ItemPage(browser, link)
    page.open()

    item_name = page.get_item_name()

    page.click_add_to_basket()

    added_to_basket_msg = page.get_item_added_to_basket_message()
    assert f"{item_name} has been added to your basket." == added_to_basket_msg, ("Basked added message shows item "
                                                                                  "name correctly")


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    item_page = ItemPage(browser, link)
    item_page.open()

    item_page.open_basket()

    basket_page = BasketPage(browser, link)
    assert basket_page.is_not_element_present(BasketPageLocators.ITEM_NAMES), "There are no elements in the basket"

    assert "Your basket is empty." in basket_page.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, \
        "Basket empty text is shown"
