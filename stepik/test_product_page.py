from links.links import ProjectLinks
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('link', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                  pytest.param("offer7", marks=pytest.mark.xfail),
                                  "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	url = f"{ProjectLinks.PROMO_LINK_TEMPLATE}{link}"
	product_page = ProductPage(browser, url)
	product_page.open()
	product_page.should_be_product_page()
	data = product_page.get_product_name_and_price()
	product_page.add_to_basket()
	product_page.solve_quiz_and_get_code()
	product_page.check_product_added_to_basket(*data)


@pytest.mark.xfail(reason="Success message appears, while should not.")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	product_page = ProductPage(browser, ProjectLinks.NO_PROMO_PRODUCT_LINK)
	product_page.open()
	product_page.add_to_basket()
	product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
	product_page = ProductPage(browser, ProjectLinks.NO_PROMO_PRODUCT_LINK)
	product_page.open()
	product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Element does not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
	product_page = ProductPage(browser, ProjectLinks.NO_PROMO_PRODUCT_LINK)
	product_page.open()
	product_page.add_to_basket()
	product_page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProjectLinks.PROD_LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProjectLinks.PROD_LINK)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, ProjectLinks.PROD_LINK)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProjectLinks.PROD_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, ProjectLinks.PROD_LINK)
    basket_page.should_be_basket_page()
    basket_page.should_not_have_products_added()
    basket_page.should_have_empty_basket_message()