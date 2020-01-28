from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv, string
from selenium.webdriver.common.keys import Keys
from difflib import SequenceMatcher
from util import Final, get_index_for_classification, load_json_file
from collections import OrderedDict 
import json


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

driver = webdriver.Chrome("/Users/pr/Desktop/capstone/fintech/chromedriver")
driver.get("https://materiality.sasb.org/")

time.sleep(3)

def load_element(driver, element, attr_key, attr_value):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sub_soup = soup.find(element, attrs={attr_key: attr_value})
    # print(issues_soup)
    return sub_soup


def get_issue_occupancy_list(driver):
    soup = load_element(driver, "tbody", "id", "mainBody")
    sasb_issues_json = load_json_file("sasb_issues.json")
    sasb_headers_json = load_json_file("sasb_headers.json")
    rows = soup.find_all("tr")
    sasb_headers = sasb_headers_json.keys()
    sasb_issues = sasb_issues_json.keys()
    print(len(rows))
    for i in range(len(rows)):
        sub_headers = sasb_issues[i]
        
        cols = rows[i].find_all("td")

    print("Heelooo")

def obj_dict(obj):
    return obj.__dict__
    
get_issue_occupancy_list(driver)

driver.close()
