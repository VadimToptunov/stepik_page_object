from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
	PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
	PRODUCT_GALLERY_IMAGE = (By.CSS_SELECTOR, ".carousel#product_gallery img")
	PRICE = (By.CSS_SELECTOR, ".price_color")
	IN_STOCK_AVAILABILITY = (By.CSS_SELECTOR, ".instock.availability")
	WRITE_REVIEW_BUTTON = (By.CSS_SELECTOR, "#write_review")
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
	ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-wishlist")
	PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".sub-header#product_description~p")
	PRODUCT_ADDED_ELEMENT = (By.CSS_SELECTOR, ".alertinner")
		
		