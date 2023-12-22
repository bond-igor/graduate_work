import yaml
import time
from testpage import OperationsHelper
import logging


with open("testdata.yaml", encoding='utf-8') as f:
	testdata = yaml.safe_load(f)


#проверка загрузки главной страницы
def test_loading_site(browser):
	logging.info("Тест  проверки загрузки страницы запущен")
	testpage = OperationsHelper(browser, testdata["url"])
	testpage.go_to_site()
	assert testpage.loading_site() == testdata["title"]


#отображение емейла
def test_email(browser):
	logging.info("Тест проверки отображения email запущен")
	testpage = OperationsHelper(browser, testdata["url"])
	testpage.go_to_site()
	assert testpage.email() == testdata["email"]

#отображение телефона
def test_phone(browser):
	logging.info("Тест проверки отображения телефона запущен")
	testpage = OperationsHelper(browser, testdata["url"])
	testpage.go_to_site()
	assert testpage.phone() == testdata["phone"]

#отображение адреса
def test_address(browser):
	logging.info("Тест проверки отображения адреса запущен")
	testpage = OperationsHelper(browser, testdata["url"])
	testpage.go_to_site()
	assert testpage.address() == testdata["address"]

#проверка функционирования чата (только в рабочие часы)
def test_omjet(browser):
	logging.info("Тест проверки чата запущен")
	testpage = OperationsHelper(browser, testdata["url"])
	testpage.go_to_site()
	testpage.click_widget()
	testpage.click_omjet()
	testpage.omjet_input(testdata["chat_message"])
	testpage.click_omjet_enter()
	time.sleep(testdata["sleep_time"])
	result = testpage.omjet_result()
	testpage.click_omjet_close()
	assert result == testdata["chat_message"]

#Проверка функционирования обратного звонка (только в рабочие часы)
def test_callback(browser):
	logging.info("Тест проверки заказа обратного звонка запущен")
	testpage = OperationsHelper(browser, testdata["url"])
	testpage.go_to_site()
	testpage.click_widget()
	testpage.click_phone_btn()
	testpage.phone_input(testdata["test_phone"])
	testpage.click_call_btn()
	time.sleep(testdata["sleep_time"])
	phone_result = testpage.phone_result()
	testpage.click_phone_close()
	assert phone_result == testdata["phone_confirmation"]

#проверка формы обратной связи
def test_feedback(browser):
	logging.info("Тест проверки формы обратной связи запущен")
	testpage = OperationsHelper(browser, testdata["url"])
	testpage.go_to_site()
	try:
		testpage.click_widget()
	except:
		pass
	testpage.click_feedback_btn()
	testpage.feedback_input_name(testdata["name"])
	testpage.feedback_input_surname(testdata["surname"])
	testpage.feedback_input_phone(testdata["test_phone"])
	testpage.feedback_input_email(testdata["test_email"])
	testpage.click_feedback_send_btn()
	time.sleep(testdata["sleep_time"])
	feedback_result = testpage.feedback_result()
	time.sleep(testdata["sleep_time"])
	assert feedback_result == testdata["feedback_confirmation"]
