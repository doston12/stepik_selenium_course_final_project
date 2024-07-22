import time

import pytest

from pages.item_page import ItemPage
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

    def test_user_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ItemPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_user_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ItemPage(browser, link)
        page.open()

        page.go_to_login_page()
        assert "login" in page.browser.current_url, "Login page opened"
