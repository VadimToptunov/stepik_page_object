from pages.main_page import MainPage
from pages.login_page import LoginPage
from links.links import ProjectLinks

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, ProjectLinks.MAIN_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


def test_guest_can_see_correct_login_page(browser):
    page = MainPage(browser, ProjectLinks.MAIN_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page = LoginPage(browser, ProjectLinks.MAIN_PAGE_LINK)
    login_page.should_be_login_page()