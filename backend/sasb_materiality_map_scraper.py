from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv, string
from selenium.webdriver.common.keys import Keys
from difflib import SequenceMatcher
from util import Final

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

driver = webdriver.Chrome("/home/koshy/Desktop/Capstone/fintech/chromedriver")
driver.get("https://materiality.sasb.org/")

time.sleep(3)


def load_issues(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    issues_soup = soup.find('tbody', attrs={'id': 'frozenBody'})
    print(issues_soup)

load_issues(driver)

# def load_results_for_ticker(driver, elem, ticker):
#     elem.clear()
    
#     elem.send_keys(ticker)

#     elem.send_keys(Keys.RETURN)
#     time.sleep(3)

#     tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')
#     tutorial_code_soup = tutorial_soup.find_all('div', attrs={'id': 'company-search-response'})

#     # print(tutorial_code_soup[0].find("tbody"))
#     tbody = tutorial_code_soup[0].find("tbody")
#     if tbody == None:
#         return None
#     return tbody.findChildren("tr")

# with open("output.csv", "a") as output:
#     writer = csv.writer(output, lineterminator='\n', delimiter='|')

#     with open('/home/koshy/Desktop/Capstone/fintech/data/result.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter='|')
#         sic_list = []

#         for r in csv_reader:
#             ticker = r[1]
#             company = r[2]
#             results = load_results_for_ticker(driver, elem, ticker)
#             isin = None
#             sics_sector = None
#             sics_industry = None
#             if results != None:
#                 for val in results[:-1]:
#                     tds = val.findChildren("td")
#                     new = tds[2].getText().translate(str.maketrans('', '', string.punctuation))
#                     orig = company.translate(str.maketrans('', '', string.punctuation))
#                     v = similar(new.lower(), orig.lower())
#                     # print(v)
#                     if v > 0.7:
#                         isin = tds[1].getText()
#                         sics_sector = tds[3].getText()
#                         sics_industry = tds[4].getText()
#                         break
#             if isin == None:
#                 print(f"{ticker} {company}")
#             r.append(isin)
#             r.append(sics_sector)
#             r.append(sics_industry)
#             # print(r)
#             writer.writerow(r)
#             sic_list.append(r)
#         # break
driver.close()
