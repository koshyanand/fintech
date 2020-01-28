from flashtext import KeywordProcessor
from util import get_data_with_code, load_csv

def search_for_keyword(keywords, text):
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(keywords)
    keywords_found = keyword_processor.extract_keywords(text)
    return set(keywords_found)


df = load_csv("data/output.csv", "|")
# print(df)
sub_df, sec_data_list = get_data_with_code("sasb", df, "Internet Media & Services")
words = ["cybersecurity", "hacker", "data security"]
result_list  =  list(map(lambda text: search_for_keyword(words, text), sec_data_list))
print(result_list)