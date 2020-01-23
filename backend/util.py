import pandas as pd

header = "Item&nbsp;"


class Final:
    def __init__(self, cik, ticker, company, filing_date, file_path, exchange, sic, isin, sics_sector, sics_industry):
        self.cik = cik 
        self.ticker = ticker
        self.company = company
        self.filing_date = filing_date
        self.file_path = file_path
        self.exchange = exchange
        self.sic = sic
        self.isin = isin
        self.sics_sector = sics_sector
        self.sics_industry = sics_industry
    
        
    def __str__(self):
        val = f"{str(self.cik)}|{self.ticker}|{self.company}|{self.filing_date}|{self.exchange}|{self.sic}|{self.isin}|{self.sics_sector}|{self.sics_industry}|{self.file_path}"
        return val

def get_item_combinations(section_no_list):
    partition_list = []
    df = pd.read_csv('data/item_list.csv')

    shape = df.shape
    item_list = df.values.tolist()
    for section in section_no_list:
        for i, row in enumerate(item_list):  
            if row[0] == section:
                start = section
                if i + 1 < shape[0]: 
                    end = item_list[i + 1][0]
                else:
                    end = None
                partition_list.append((start, end))
    return partition_list


def get_raw_section(full_text, section_no_list):
    partition_list = get_item_combinations(section_no_list)
    section = []
    for partition in partition_list:
        start, end = partition
        print(header + start)
        start_pos = full_text.find(header + start)
        print(start_pos)
        if end != None:
            end_pos = full_text.find(header + end)
        print(end_pos)
        section.append(full_text[start_pos : end_pos])
    return section
    # print(partition_list)

def load_10k_info(path):
    df = pd.read_csv(path, sep='|'  , engine='python')
    return df

def get_header_for_classification(type, file_path):

    df = pd.read_csv(file_path, sep='|'  , engine='python')
    print(df)
    # if type == "sic":

get_header_for_classification("sic", "data/sasb_codes.csv")



def get_data_with_code(type, sec_10k_df, *args):
    
    if type == "sic":
        sic_code = args[0]
    else:
        industry, sector = args[0], args[1]
    





    

