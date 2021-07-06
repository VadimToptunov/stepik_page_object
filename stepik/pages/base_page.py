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


	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		return True


	def quit(self):
		self.browser.quit()
		