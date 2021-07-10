from links.links import ProjectLinks
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest
import time

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
