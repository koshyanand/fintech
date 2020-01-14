# from SECEdgar.filings import Filing, FilingType
# my_filings = Filing(cik='0001113232', filing_type=FilingType.FILING_10K) # 10-Q filings for Apple (NYSE: AAPL)
# my_filings.save('~/Desktop/fintech/data')

from bs4 import BeautifulSoup
from util import get_raw_section

file1 = open("data/0000320193/10-k/0000320193-17-000070.txt", "r") 

data = str(file1.read())
print(data.find("<DESCRIPTION>GRAPHIC"))
data = data[-1 : data.find("<DESCRIPTION>GRAPHIC")]
print(get_raw_section(data, ["1A"]))



# print(data)
# Risk Factors    
page = open("data/0000320193/10-k/0000320193-17-000070.txt")
soup = BeautifulSoup(page.read())
# print(soup)

