class BasePage(object):
	"""
	Base page for Page Object Model Selenium tests witth Python.
	"""
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url


	def open(self):
		self.browser.get(self.url)


	def quit(self):
		self.browser.quit()
		