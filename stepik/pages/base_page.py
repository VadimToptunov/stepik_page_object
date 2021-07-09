import math
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    """
    Base page for Page Object Model Selenium tests witth Python.
    """

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)


    def find(self, how, what):
        return self.browser.find_element(how, what)


    def get_element_text(self, how, what):
        return self.find(how, what).text


    def is_element_present(self, how, what):
        try:
            self.find(how, what)
        except NoSuchElementException:
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
