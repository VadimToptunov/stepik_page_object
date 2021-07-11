from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_HEADER = (By.CSS_SELECTOR, ".page-header.action h1")
	BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
	BASKET_SUMMARY_ELEMENT = (By.CSS_SELECTOR, ".basket_summary#basket_formset")	
	BASKET_BREAD_CRUMB = (By.CSS_SELECTOR, ".breadcrumb .active")
	BASKET_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.navbar-btn.btn-cart")
	

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary[name='registration_submit']")


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
	BASKET_TOTAL_ELEMENT = (By.CSS_SELECTOR, ".alertinner p")
	SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success")
