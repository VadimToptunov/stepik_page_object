import math
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from .locators import BasePageLocators

class BasePage(object):
    """
    Base page for Page Object Model Selenium tests witth Python.
    """

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url


    def open(self):
        self.browser.get(self.url)


    def find(self, how, what):
        return self.browser.find_element(how, what)


    def get_element_text(self, how, what):
        return self.find(how, what).text


    def go_to_login_page(self):
        link = self.find(*BasePageLocators.LOGIN_LINK)
        link.click()


    def go_to_basket(self):
        self.find(*BasePageLocators.VIEW_BASKET_BUTTON).click()


    def is_element_present(self, how, what):
        try:
            self.find(how, what)
        except NoSuchElementException:
            return False
        return True


    def is_not_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def is_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_src_not_empty(self, how, what):
        try:
            element_src = self.find(how, what).get_attribute("src")
            if element_src == "" or element_src == None:
                return False
        except NoSuchElementException:
            return False
        return True


    def is_element_text_not_empty(self, how, what):
        try:
            element_text = self.get_element_text(how, what)
            if element_text == "" or element_text == None:
                return False
        except NoSuchElementException:
            return False
        return True


    def is_url_correct(self, pattern):
        if pattern in str(self.browser.current_url):
            return True
        else: 
            return False


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user."


    def generate_random_string(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))


    def generate_credentials(self):
        body = self.generate_random_string()
        return (f"{body}@fakemail.com", self.generate_random_string())


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
