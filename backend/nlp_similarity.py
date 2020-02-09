import pandas
from util import load_json_file, get_data_with_code, load_csv, get_value_from_json
from nlp import preprocess, get_jaccard_sim
import spacy
nlp = spacy.load('en')

df = load_csv("data/output.csv", "|")
# print(df)

industry_json = load_json_file("sasb_mm_industry.json")
threat_json = load_json_file("sasb_mm_threats.json")

sub_df, sec_data_list = get_data_with_code("sasb", df, "Internet Media & Services")
# print(sec_data_list[0])
text_data = []

for data in sec_data_list:
    tokens = preprocess(data)
    # print(tokens)
    text_data.append(tokens)

threat_desc = []
threat_name = []

for data in sec_data_list:
    doc1 = nlp(data)
    for threat in threat_json:
        print(threat["Threat"])
        for obj in threat["SubThreats"]:
            doc2 = nlp(obj["Description"])
            print(obj["SubThreat"])
            threat_desc.append(preprocess(obj["Description"]))
            threat_name.append(obj["SubThreat"])
            print(doc1.similarity(doc2))
    break
    jaccard_val = []
# cosine_val = []


# for text in text_data:
#     # print(text)
#     for i, threat in enumerate(threat_desc):
#         jv = get_jaccard_sim(threat, text)
#         print(threat_name[i] + " jv : " + str(jv))
#         jaccard_val.append(jv)
#     break

# print(jaccard_val)


