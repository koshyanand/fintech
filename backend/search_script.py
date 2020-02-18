from flashtext import KeywordProcessor
from util import get_data_with_code, load_csv, load_json_file
from nlp import preprocess

def search_for_keyword(keywords, text):
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(keywords)
    keywords_found = keyword_processor.extract_keywords(text)
    return list(set(keywords_found))

df = load_csv("data/output.csv", "|")


industry_json = load_json_file("sasb_mm_industry.json")
threat_json = load_json_file("sasb_mm_threats.json")

sub_df, sec_data_list = get_data_with_code("sasb", df, "Semiconductors")
# print(sec_data_list[0])
text_data = []

threat_list = []
for threat in threat_json:
    for obj in threat["SubThreats"]:
        # tokens = preprocess(obj["SubThreat"])
        tokens = []
        tokens.append(obj["SubThreat"])
        threat_list.append(tokens)
words = ["cybersecurity", "hacker", "data security"]
# print(threat_list)
result_list = []
for data in sec_data_list:
    
    for threats in threat_list:
        # print(threats)
        vals = search_for_keyword(threats, data)
        result_list.append(vals)

# result_list  =  list(map(lambda text: search_for_keyword(threat_list, text), sec_data_list))
print(result_list)
print(len(sec_data_list))
print(len(result_list))

print("len : " + str(len(threat_list)))
