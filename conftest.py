import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
	testdata = yaml.safe_load(f)

@pytest.fixture()
def title():
	return """//*[@id="b5538"]/section/div/h2/p[1]/span"""

@pytest.fixture()
def email():
	return """//*[@id="navBar5598"]/ul/li[1]/a"""

@pytest.fixture()
def phone():
	return """//*[@id="navBar5598"]/ul/li[3]/a"""

@pytest.fixture()
def address():
	return """//*[@id="navBar5598"]/ul/li[2]/a"""

@pytest.fixture()
def widget():
	return """/html/body/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[1]"""
@pytest.fixture()
def omjet():
	return """/html/body/div[2]/div/div[3]/div[2]/a[1]"""

@pytest.fixture()
def omjet_input():
	return """/html/body/div[1]/div/div/div[4]/div[2]/div[1]/textarea"""

@pytest.fixture()
def omjet_enter():
	return """/html/body/div[1]/div/div/div[4]/div[2]/div[1]/button"""

@pytest.fixture()
def omjet_result():
	return """/html/body/div[1]/div/div/div[5]/div/div/div/div/div/div/div[1]/div[1]/div"""

@pytest.fixture()
def omjet_close():
	return """/html/body/div[1]/div/div/div[2]/div/div[3]/button"""

@pytest.fixture()
def phone_btn():
	return """/html/body/div[2]/div/div[3]/div[2]/a[2]"""

@pytest.fixture()
def phone_input():
	return """//*[@id="b24-b24-site-button-form-72"]/div/div[2]/div/div/div[2]/form/div[1]/div/div/div/div/input"""

@pytest.fixture()
def call_btn():
	return """//*[@id="b24-b24-site-button-form-72"]/div/div[2]/div/div/div[2]/form/div[3]/div/button"""

@pytest.fixture()
def phone_result():
	return """//*[@id="b24-b24-site-button-form-72"]/div/div[2]/div/div/div[3]/div[2]/div[1]/div[2]"""

@pytest.fixture()
def phone_close():
	return """//*[@id="b24-b24-site-button-form-72"]/div/div[2]/button"""

@pytest.fixture(scope="module")
def site():
	my_site = Site(testdata["url"])
	yield my_site
	#my_site.close()
