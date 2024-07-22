
import pytest

from pages.basket_page import BasketPage
from pages.item_page import ItemPage
from utils.QuizUtil import solve_quiz_and_get_code


@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
def test_guest_can_go_to_login_page(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    item_page = ItemPage(browser, link)
    item_page.open()

    item_price = item_page.get_item_price()
    item_name = item_page.get_item_name()

    item_page.click_add_to_basket()

    solve_quiz_and_get_code(item_page.browser)

    added_to_basket_msg = item_page.get_item_added_to_basket_message()
    assert f"{item_name} has been added to your basket." == added_to_basket_msg, ("Basked added message shows item "
                                                                                  "name correctly")

    item_page.open_basket()

    basket_page = BasketPage(browser, link)
    assert item_price == basket_page.get_basket_total(), "Basket total shows correct amount"
    assert item_name == basket_page.get_basket_item_names()[0], "Basket shows item name correctly"


