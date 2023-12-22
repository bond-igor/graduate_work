from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import requests

with open("testdata.yaml") as f:
	test_data = yaml.safe_load(f)

class TestSearchLocators:
	dictloc = dict()
	with open("locators.yaml") as f:
		locators = yaml.safe_load(f)
	for locator in locators["xpath"].keys():
		dictloc[locator] = (By.XPATH, locators["xpath"][locator])
	for locator in locators["css"].keys():
		dictloc[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):

	def enter_text_into_field(self, locator, word, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		logging.info(f"Отправлено '{word}' элементу {element_name}")
		field = self.find_element(locator)
		if not field:
			logging.error(f"Элемент {locator} не найден")
			return False
		try:
			field.clear()
			field.send_keys(word)
		except:
			logging.exception(f"исключение при работе с {locator}")
			return False
		return True

	def get_text_from_element(self, locator, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		field = self.find_element(locator, time=10)
		if not field:
			return None
		try:
			text = field.text
		except:
			logging.exception(f'Исключение при получении теста из {element_name}')
			return None
		logging.info(f'Мы находим текст {text} в поле {element_name}')
		return text

	def click_button(self, locator, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		button = self.find_element(locator)
		if not button:
			return False
		try:
			button.click()
		except:
			logging.exception(f'Исключение при клике')
			return False
		logging.info(f'Нажимаем {element_name} кнопку')
		return True

#Получение текста
	def loading_site(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["title"])

	def email(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["email"])

	def phone(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["phone"])

	def address(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["address"])

	def omjet_result(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["omjet_result"])

	def phone_result(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["phone_result"])

	def feedback_result(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["feedback_result"])


#Ввод текста
	def omjet_input(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["omjet_input"], word, description="Chat")

	def phone_input(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["phone_input"], word, description="phone")

	def feedback_input_name(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["feedback_input_name"], word, description="feedback_input_name")

	def feedback_input_surname(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["feedback_input_surname"], word, description="feedback_input_surname")

	def feedback_input_phone(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["feedback_input_phone"], word, description="feedback_input_phone")

	def feedback_input_email(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["feedback_input_email"], word, description="feedback_input_email")



#Нажатия кнопок
	def click_widget(self):
		self.click_button(TestSearchLocators.dictloc["widget"], description="widget")

	def click_omjet(self):
		self.click_button(TestSearchLocators.dictloc["omjet"], description="Omjet")

	def click_omjet_enter(self):
		self.click_button(TestSearchLocators.dictloc["omjet_enter"], description="Enter")

	def click_omjet_close(self):
		self.click_button(TestSearchLocators.dictloc["omjet_close"], description="Close")

	def click_phone_btn(self):
		self.click_button(TestSearchLocators.dictloc["phone_btn"], description="phone_btn")

	def click_call_btn(self):
		self.click_button(TestSearchLocators.dictloc["call_btn"], description="call_btn")

	def click_phone_close(self):
		self.click_button(TestSearchLocators.dictloc["phone_close"], description="phone_close")

	def click_feedback_btn(self):
		self.click_button(TestSearchLocators.dictloc["feedback_btn"], description="feedback_btn")

	def click_feedback_send_btn(self):
		self.click_button(TestSearchLocators.dictloc["feedback_send_btn"], description="feedback_send_btn")

