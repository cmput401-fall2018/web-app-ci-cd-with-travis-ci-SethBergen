from selenium import webdriver
from selenium.webdriver.common.key import keys

def test_home():
	driver = webdriver.Chrome()
	driver.get("http://127.0.0.1:8000")
	elem = driver.find_element_by_id("name")
	assert elem != None 
