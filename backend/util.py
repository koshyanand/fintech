import pandas as pd
from collections import OrderedDict 
import json 
header = "Item&nbsp;"
from bs4 import BeautifulSoup

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

def load_element(driver, element, attr_key, attr_value):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sub_soup = soup.find(element, attrs={attr_key: attr_value})
    return sub_soup

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

def save_json_to_file(file_name, file_path, json_data):
    with open(file_path + file_name, 'w') as outfile:
        json.dump(json_data, outfile, indent=2)

def load_csv(path, delimiter):
    df = pd.read_csv(path, sep=delimiter  , engine='python')
    return df

def get_index_for_classification(type, file_path):
    df = load_csv(file_path, "|")
    index = OrderedDict() 
    if type == "sic":
        header = "Office"
        sub_header = "Industry"
        code = "SIC"

    elif type == "sasb":
        header = "Sector"
        sub_header = "Industry"
        code = "Id"
    
    else:
        return None

    headers = df[header].unique()
    for h in headers:
        sub_df = df[pd.eval("df[header] == h")]
        index[h] = list(zip(sub_df[code], sub_df[sub_header]))
    
    return index

def load_txt_file(head_path, path):
    with open(head_path + path, 'r') as content_file:
        content = content_file.read()
        return content

def load_json_file(path):
    with open(path) as json_file:
        return json.load(json_file)
        

def get_data_with_code(type, sec_10k_df, *args):
    
    if type == "sic":
        sic_code = args[0]
        sub_df = sec_10k_df[pd.eval('sec_10k_df["SIC"] == sic_code')]
    else:
        industry = args[0]
        sub_df = sec_10k_df[pd.eval('sec_10k_df["SASB Idustry"] == industry')]

    # print(sub_df)
    files = sub_df.Directory.tolist()

    risk_data_list = list(map(lambda path: load_txt_file("data/SEC/", path), files))
    # print(len(risk_data_list))
    # print(risk_data_list)

    return sub_df, risk_data_list

def get_value_from_json(json_array, head, head_value, array_head, sub_head, sub_head_value):

    for obj in json_array:
        if obj[head] == head_value:

            if array_head == None:
                return obj
            
            for sub in obj[array_head]:
                
                if sub[sub_head] == sub_head_value:
                    return sub




    
    

    





    

