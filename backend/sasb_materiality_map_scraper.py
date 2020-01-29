from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv, string
from selenium.webdriver.common.keys import Keys
from difflib import SequenceMatcher
from util import Final, get_index_for_classification, load_json_file, save_json_to_file, load_element
from collections import OrderedDict 
import json
import copy

driver = webdriver.Chrome("/home/koshy/Desktop/Capstone/fintech/chromedriver")
driver.get("https://materiality.sasb.org/")

time.sleep(3)



def set_threat_map(sasb_sector, sasb_industry, sasb_threat, sasb_sub_threat, threat_json):
    for threat in threat_json:
        if threat["Threat"] == sasb_threat:
            for sub_threat in threat["SubThreats"]:
                if sub_threat["SubThreat"] == sasb_sub_threat:
                    if "Industries" not in sub_threat:
                        sub_threat["Industries"] = []

                    sub_threat["Industries"].append({"Sector" : sasb_sector, "Industry" : sasb_industry["Industry"]})
    # print(threat_json)  
    
def set_industry_map(sasb_sector, sasb_industry, sasb_threat, sasb_sub_threat, industry_json):
    print(sasb_sector, sasb_industry)
    for sector in industry_json:
        if sector["Sector"] == sasb_sector:
            for industry in sector["Industries"]:
                if industry["Industry"] == sasb_industry["Industry"]:
                    if "Threats" not in industry:
                        industry["Threats"] = []
                    # print(sasb_threat, sasb_sub_threat)
                    industry["Threats"].append({"Threat" : sasb_threat, "SubThreat" : sasb_sub_threat})


def set_row_data(sasb_threat, sasb_sub_threat, row, sasb_industries, industry_json, threat_json):
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
        # print(sector, industry, col)

        if col["class"][0].find("manyMaterial") != -1:
            # set_threat_map(sector, industry, sasb_threat, sasb_sub_threat, threat_json)
            set_industry_map(sector, industry, sasb_threat, sasb_sub_threat, industry_json)
        k += 1
    
  
        


def get_threat_occupancy_list(driver):
    soup = load_element(driver, "tbody", "id", "mainBody")
    sasb_threats_json = load_json_file("sasb_threats.json")
    sasb_sector_json = load_json_file("sasb_codes.json")
    rows = soup.find_all("tr")

    sasb_threat_centric = copy.deepcopy(sasb_threats_json)

    sasb_industry_centric = copy.deepcopy(sasb_sector_json)

    j = 0
    k = 0
    for i in range(len(rows)):
        sasb_threat = sasb_threats_json[j]

        cols = rows[i].find_all("td")
        set_row_data(sasb_threat["Threat"], sasb_threat["SubThreats"][k]["SubThreat"], cols, sasb_sector_json, sasb_industry_centric, sasb_threat_centric)
        
        k += 1
        if len(sasb_threat["SubThreats"]) <= k:
                k = 0
                j += 1
        # break
    
    save_json_to_file("sasb_mm_industry.json", "", sasb_industry_centric)
    save_json_to_file("sasb_mm_threats.json", "", sasb_threat_centric)


get_threat_occupancy_list(driver)

driver.close()
