import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#загружаем конфигурационные данные в словарь
with open("./testdata.yaml") as f:
	testdata = yaml.safe_load(f)
browser = testdata["browser"]

class Site:
	def __init__(self, address):
		#инициализация браузера firefox
		if browser == "firefox":
			service = Service(testdata["driver_path_firefox"])
			options = webdriver.FirefoxOptions()
			self.driver = webdriver.Firefox(service=service, options=options)
			self.driver.implicitly_wait(10)
		#инициализация браузера chrome
		elif browser == "chrome":
			service = Service(testdata["driver_path_chrom"])
			options = webdriver.ChromeOptions()
			self.driver = webdriver.Chrome(service=service, options=options)
			self.driver.implicitly_wait(10) #время ожидания появления элемента
			self.driver.maximize_window()
			self.driver.get(address)
			time.sleep(testdata["sleep_time"])

#функция поиска элементов страницы по xpath или css
	def find_element(self, mode, path):
		if mode == "css":
			element = self.driver.find_element(By.CSS_SELECTOR, path)
		elif mode == "xpath":
			element = self.driver.find_element(By.XPATH, path)
		else:
			element = None
		return element

#функция для получения имеющихся свойств элемента
	def get_element_property(self, mode, path, property):
		element = self.find_element(mode, path)
		return element.value_of_css_property(property)

	def close(self):
		self.driver.close()





