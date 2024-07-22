from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login-form")
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.ID, "registration-form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class ItemPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']//button[@type='submit']")
    ITEM_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]//p[@class='price_color']")
    ITEM_ADDED_BASKET_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]")
    ITEM_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")


class BasketPageLocators():
    BASKET_TOTAL = (By.XPATH, "//th[normalize-space()='Basket total']/following-sibling::th")
    SHIPPING_TOTAL = (By.XPATH, "//th[normalize-space()='Free shipping']/following-sibling::th")
    ITEM_NAMES = (By.XPATH, "//div[@class='basket-items']//div/h3/a")
