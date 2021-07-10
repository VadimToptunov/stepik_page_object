from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
	    self.should_be_basket_url()
	    self.should_have_basket_bread_crumb_text_basket()
	    self.should_have_basket_navbar()


    def should_be_basket_url(self):
	    basket_end = "basket"
	    assert self.is_url_correct(basket_end), "URL for basket page is incorrect."


    def should_have_basket_navbar(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NAVBAR_BUTTON), "No basket_navbar button presents."


    def should_have_basket_bread_crumb_text_basket(self):
        actual_result = self.get_element_text(*BasketPageLocators.BASKET_BREAD_CRUMB) 
        expected_result ="Basket"
        assert actual_result == expected_result, f"'{actual_result}' is not equal to '{expected_result}'."


    def should_have_empty_basket_message(self):
        actual_result = self.get_element_text(*BasketPageLocators.BASKET_IS_EMPTY)
        expected_result = "Your basket is empty. Continue shopping"
        assert actual_result == expected_result, f"'{actual_result}' is not equal to '{expected_result}'."


    def should_not_have_products_added(self):
	    assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_ELEMENT), "The basket is not empty"
		