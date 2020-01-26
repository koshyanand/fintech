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

driver = webdriver.Chrome("/Users/pr/Desktop/capstone/fintech/chromedriver")
driver.get("https://materiality.sasb.org/")

time.sleep(3)

class SubIssue:
    def __init__(self, sub_issue, description):
        self.sub_issue = sub_issue
        self.description = description
    
    def __str__(self):
        print(self.sub_issue + " Desc : " + self.description)

class Issue:
    def __init__(self, issue, description):
        self.issue = issue
        self.description = description
        self.sub_issues = []

    def __str__(self):
        print(self.issue + " Desc : " + self.description)
        print(self.sub_issues)


def load_issues(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    issues_soup = soup.find('tbody', attrs={'id': 'frozenBody'})
    # print(issues_soup)
    return issues_soup

def get_issue_sub_issue(soup):
    rows = soup.find_all('tr')
    issue_list = []
    print(len(rows))
    
    sub_issue_map = {}
    head_issue = None
    is_obj = None
    for i, r in enumerate(rows):
        issue = r.find('th', attrs={'style': 'background: white !important; vertical-align:middle; font-weight:normal !important'})
        sub_issue = r.find('th', attrs={'style':'line-height:10px; min-height:10px; height:10px; white-space:nowrap; left:64px; font-weight: normal !important'})
        # print(issue)
        if issue != None:

            issue_desc = issue.find('span')['title']
            issue_title = issue.find('span').getText()

            if is_obj != None:
                issue_list.append(is_obj)

            is_obj = Issue(issue_title, issue_desc)

        sub_issue_desc = sub_issue.find('span')['title']
        sub_issue_title = sub_issue.find('span').getText()

        si_obj = SubIssue(sub_issue_title, sub_issue_desc)
        is_obj.sub_issues.append(si_obj)
        # print(iss)
        # break
    issue_list.append(is_obj)
    return issue_list

issues = load_issues(driver)

print(len(get_issue_sub_issue(issues)))



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
