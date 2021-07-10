from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
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


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    test_guest_cant_see_product_in_basket_opened_from_main_page:

    Гость открывает главную страницу 
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста 

    """
    page = MainPage(browser, ProjectLinks.MAIN_PAGE_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, ProjectLinks.MAIN_PAGE_LINK)
    basket_page.should_be_basket_page()
    basket_page.should_not_have_products_added()
    basket_page.should_have_empty_basket_message()