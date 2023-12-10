import yaml
import time


with open("testdata.yaml", encoding='utf-8') as f:
	testdata = yaml.safe_load(f)


#проверка загрузки главной страницы
def test_loading_site(title, site):
	title = site.find_element("xpath", title)
	assert title.text == testdata["title"]

#отображение емейла
def test_email(email, site):
	email = site.find_element("xpath", email)
	assert email.text == testdata["email"]

#отображение телефона
def test_phone(phone, site):
	phone = site.find_element("xpath", phone)
	assert phone.text == testdata["phone"]

#отображение адреса
def test_address(address, site):
	address = site.find_element("xpath", address)
	assert address.text == testdata["address"]

#проверка функционирования чата
def test_omjet(site, widget, omjet, omjet_input,omjet_enter, omjet_result, omjet_close):
	widget = site.find_element("xpath", widget)
	widget.click()
	omjet = site.find_element("xpath", omjet)
	omjet.click()
	input_text = site.find_element("xpath", omjet_input)
	input_text.send_keys(testdata["chat_message"])
	enter = site.find_element("xpath", omjet_enter)
	enter.click()
	time.sleep(testdata["sleep_time"])
	result = site.find_element("xpath", omjet_result)
	close = site.find_element("xpath", omjet_close)
	close.click()
	assert result.text == testdata["chat_message"]

#Проверка функционирования обратного звонка
def test_callback(site, widget, phone_btn,phone_input, call_btn, phone_result, phone_close):
	widget = site.find_element("xpath", widget)
	widget.click()
	phone_btn = site.find_element("xpath", phone_btn)
	phone_btn.click()
	phone_input = site.find_element("xpath", phone_input)
	phone_input.send_keys(testdata["test_phone"])
	call_btn = site.find_element("xpath", call_btn)
	call_btn.click()
	time.sleep(testdata["sleep_time"])
	phone_result = site.find_element("xpath", phone_result)
	time.sleep(testdata["sleep_time"])
	phone_close = site.find_element("xpath", phone_close)
	phone_close.click()
	assert phone_result.text == testdata["phone_confirmation"]

#проверка формы обратной связи

