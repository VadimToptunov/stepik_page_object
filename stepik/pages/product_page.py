from pages.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
    	self.should_be_product_link()
    	self.should_present_product_gallery_image()
    	self.price_should_be_present()
    	self.should_present_in_stock_availability()
    	self.should_present_write_review_button()
    	self.should_present_add_to_basket_button()
    	self.product_description_is_not_empty()

    def should_be_product_link(self):
    	product_url_part = "catalogue"
    	self.is_url_correct(product_url_part), "URL for product page is incorrect."

    def should_present_product_gallery_image(self):
    	assert self.is_element_src_not_empty(*ProductPageLocators.PRODUCT_GALLERY_IMAGE), "Product gallery image is not present on the page."


    def price_should_be_present(self):
    	assert self.is_element_text_not_empty(*ProductPageLocators.PRICE), "There's no price on the page."


    def should_present_in_stock_availability(self):
    	assert self.is_element_present(*ProductPageLocators.IN_STOCK_AVAILABILITY), "In stock availability element is not present on the page."
    

    def should_present_write_review_button(self):
    	assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW_BUTTON), "No 'Write review' button present on the page."


    def should_present_add_to_basket_button(self):
    	assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "No 'Add to basket' button present on the page."


    def should_present_add_to_wishlist_button(self):
    	assert self.is_element_present(*ProductPageLocators.ADD_TO_WISHLIST_BUTTON), "No 'Add to wishlist' button presents on the page."


    def should_not_be_success_message(self):
    	assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_ELEMENT), "Success message is presented, but should not be"


    def success_message_should_disappear(self):
    	assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_ELEMENT), "Success message is not disappeared, while it should."


    def product_description_is_not_empty(self):
    	assert self.is_element_text_not_empty(*ProductPageLocators.PRODUCT_DESCRIPTION), "Product description is empty."


    def add_to_basket(self):
    	self.find(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()


    def get_product_name_and_price(self):
    	return (self.get_element_text(*ProductPageLocators.PRODUCT_NAME), self.get_element_text(*ProductPageLocators.PRICE))


    def check_product_added_to_basket(self, product_name, price):
    	expected_product_name = f"{product_name} has been added to your basket."
    	expected_total = f"Your basket total is now {price}"
    	actual_product_name = self.get_element_text(*ProductPageLocators.PRODUCT_ADDED_ELEMENT)
    	actual_total = self.get_element_text(*ProductPageLocators.BASKET_TOTAL_ELEMENT)
    	assert (expected_product_name, expected_total) == (actual_product_name, actual_total), f"\
    	'{actual_product_name}' is not equal to '{expected_product_name}' and '{actual_total}' \
    	is not equal to '{expected_total}'"
