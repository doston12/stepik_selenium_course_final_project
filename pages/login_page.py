from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is for login page"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM).is_displayed(), "Login form visible"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM).is_displayed(), \
            "Register form visible"

    def register_new_user(self, email, password):
        self.enter_email_in_register_form(email)
        self.enter_password_register_form(password)
        self.enter_confirm_password_register_form(password)
        self.click_register()

    def enter_email_in_register_form(self, email):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)

    def enter_password_register_form(self, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)

    def enter_confirm_password_register_form(self, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)

    def click_register(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
