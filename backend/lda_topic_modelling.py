import pandas
from util import load_json_file
df = load_csv("data/output.csv", "|")
# print(df)

industry_json = load_json_file("sasb_mm_industry.json")
threat_json = load_json_file("sasb_mm_threats.json")

sub_df, sec_data_list = get_data_with_code("sasb", df, "Internet Media & Services")

text_data = []

    for line in f:
        tokens = prepare_text_for_lda(line)
        if random.random() > .99:
            print(tokens)
            text_data.append(tokens)

def clean_data()
