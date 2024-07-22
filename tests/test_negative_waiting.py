import pytest

from pages.item_page import ItemPage
from pages.locators import ItemPageLocators
from utils.QuizUtil import solve_quiz_and_get_code


@pytest.mark.xfail(reason="Success message IS presented on adding item to the basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    item_page = ItemPage(browser, link)
    item_page.open()

    item_page.click_add_to_basket()

    solve_quiz_and_get_code(item_page.browser)

    assert item_page.is_not_element_present(ItemPageLocators.ITEM_ADDED_BASKET_MESSAGE), \
        "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    item_page = ItemPage(browser, link)
    item_page.open()

    assert item_page.is_not_element_present(ItemPageLocators.ITEM_ADDED_BASKET_MESSAGE), \
        "Success message is presented, but should not be"


@pytest.mark.xfail(reason="Success message IS presented on adding item to the basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    item_page = ItemPage(browser, link)
    item_page.open()

    item_page.click_add_to_basket()

    solve_quiz_and_get_code(item_page.browser)

    assert item_page.is_disappeared(ItemPageLocators.ITEM_ADDED_BASKET_MESSAGE), \
        "Success message is presented, but should not be"
