import sqlite3
import csv

class Company:
    def __init__(self, cik, ticker, company, filing_date, file_path, exchange, sic):
        self.cik = cik 
        self.ticker = ticker
        self.company = company
        self.filing_date = filing_date
        self.file_path = file_path
        self.exchange = exchange
        self.sic = sic
    
    def __str__(self):
        val = f"{str(self.cik)}|{self.ticker}|{self.company}|{self.filing_date}|{self.exchange}|{self.sic}|{self.file_path}"
        return val

class CIK_Ticker:
    def __init__(self, cik, ticker, company, exchange, sic):
        self.cik = cik 
        self.ticker = ticker
        self.company = company
        self.exchange = exchange
        self.sic = sic


conn = sqlite3.connect("/home/koshy/Desktop/Capstone/fintech/data/SEC/metadata.sqlite3")
c = conn.cursor()
c.execute('SELECT * FROM {tn} WHERE {cn}="10-K" AND {sn}="Item1A" AND {of} is not NULL'.\
        format(tn="metadata", cn="document_group", sn="section_name", of="output_file"))
all_rows = c.fetchall()

with open('/home/koshy/Desktop/Capstone/fintech/data/MyData/cik_ticker.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    sic_list = []

    for r in csv_reader:
        # print(int(r[0]))
        # print(r[4])
        sic = None
        if r[4] != "":
            # print(r[4])
            sic = int(r[4]) 
        cik_ticker = CIK_Ticker(int(r[0]), r[1], r[2], r[3], sic)
        # sic_list.append((int(r[0]), r[1], r[2], r[3], int(r[4])))
        sic_list.append(cik_ticker)

company_list = []
for row in all_rows:
    # print(row)
    cik = int(row[5])
    found = False
    for sic in sic_list:
        if  sic.cik == cik:
            found = True
            company = Company(cik, row[6], sic.company, row[10], row[19], sic.exchange, sic.sic)
            company_list.append(company)
            break

    if not found:
        company = Company(cik, row[6], row[7], row[10], row[19], None, None)
        company_list.append(company)
        # print("CIK : " + str(cik), " company : " + row[7])
        # print("Found : " + str(found))
    # break

for company in company_list:
    print(company)