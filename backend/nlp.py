import spacy
from spacy.lang.en import English
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet as wn
import random

spacy.load('en')
parser = English()
nltk.download('wordnet')
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))

def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

def preprocess(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma2(token) for token in tokens]
    return tokens

def get_jaccard_sim(text1_list, text2_list): 
    a = set(text1_list) 
    b = set(text2_list)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def get_intersection(threat, text): 
    a = set(threat) 
    b = set(text)
    c = a.intersection(b)
    return len(c) / len(threat)
    # return float(len(c)) / (len(a) + len(b) - len(c))
