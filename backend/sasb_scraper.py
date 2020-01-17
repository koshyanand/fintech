from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/koshy/Desktop/Capstone/fintech/chromedriver")

driver.get("https://www.sasb.org/find-your-industry/")

elem = driver.find_element_by_name("searchString")
elem.clear()
elem.send_keys("AAPL")

elem.send_keys(Keys.RETURN)
time.sleep(3)

tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')
tutorial_code_soup = tutorial_soup.find_all('div', attrs={'id': 'company-search-response'})

print(tutorial_code_soup[0].find("tbody"))
