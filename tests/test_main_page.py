from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()

    main_page.open_basket()

    basket_page = BasketPage(browser, link)
    assert basket_page.is_not_element_present(BasketPageLocators.ITEM_NAMES), "There are no elements in the basket"

    assert "Your basket is empty." in basket_page.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, \
        "Basket empty text is shown"
