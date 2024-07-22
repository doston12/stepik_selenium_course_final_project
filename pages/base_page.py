import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def open_basket(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='View basket']").click()
        time.sleep(0.5)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), "Login link isn't present"

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def is_element_present(self, locator, timeout=6):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True

    def is_disappeared(self, locator, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout, 1, [TimeoutException]).
             until_not(EC.presence_of_element_located(locator)))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
