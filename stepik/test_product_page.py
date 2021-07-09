from links.links import ProjectLinks
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
	product_page = ProductPage(browser, ProjectLinks.NEW_YEAR_PROMO_LINK)
	product_page.open()
	product_page.should_be_product_page()
	product_page.find(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
	product_page.solve_quiz_and_get_code()
	product_page.check_product_added_to_basket()
