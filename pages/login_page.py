from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'url is incorrect'

    def should_be_login_form(self):
        login_form = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert len(login_form) == 1, "login form not found"

    def should_be_register_form(self):
        register_form = self.browser.find_elements(*LoginPageLocators.REGISTER_FORM)
        assert len(register_form) == 1, "register form not found"
