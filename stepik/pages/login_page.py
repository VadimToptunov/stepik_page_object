from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_end = "login"
        assert self.is_url_correct(login_end), "URL for login page is incorrect."


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present on login page."


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present on login page."


    def register_new_user(self, email, password):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        self.find(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.find(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.find(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.find(*LoginPageLocators.REGISTER_BUTTON).click()
