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

# def set_issue_map(sector, industry, issue_present):
    
# def set_industry_map(sector, industry, issue_present):


def set_row_data(sasb_sub_issue, sasb_issue_issue, row, sasb_industries, industry_map, issue_map):

    j = 0
    k = 0
    for i, col in enumerate(row):
        
        if i == 0:
            continue

        if len(sasb_industries[j]["Industries"]) <= k:
            k = 0
            j += 1
            continue
        sector = sasb_industries[j]["Sector"]
        industry = sasb_industries[j]["Industries"][k]
        print(sector, industry, col)

        issue_present = False
        if col["class"][0].find("manyMaterial") != -1:
            issue_present = True
        
        # set_issue_map(sector, industry, issue_present)
        # set_industry_map(sector, industry, issue_present)



        k += 1
        


def get_issue_occupancy_list(driver):
    soup = load_element(driver, "tbody", "id", "mainBody")
    sasb_issues_json = load_json_file("sasb_issues.json")
    sasb_sector_json = load_json_file("sasb_codes.json")
    rows = soup.find_all("tr")

    print(len(rows))
    j = 0

    industry_map = OrderedDict()

    issue_map = OrderedDict()
    k = 0
    for i in range(len(rows)):
        sasb_issue = sasb_issues_json[j]

        cols = rows[i].find_all("td")
        set_row_data(sasb_issue["Sub Issues"][k], sasb_issue["Issue"], cols, sasb_sector_json, industry_map, issue_map)
        
        k += 1
        if len(sasb_issue["Sub Issues"]) <= k:
                k = 0
                j += 1
        break



    print("Heelooo")

def obj_dict(obj):
    return obj.__dict__
    
get_issue_occupancy_list(driver)

driver.close()
