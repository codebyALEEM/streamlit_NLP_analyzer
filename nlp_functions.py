import nltk
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag,ne_chunk

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def tokenize(text):
    return word_tokenize(text)

def stem(text):
    return [stemmer.stem(token) for token  in word_tokenize(text)]

def lemmatize(text):
    return [lemmatizer.lemmatize(token) for token in word_tokenize(text)]

def pos(text):
    return pos_tag(word_tokenize(text))

def ner(text):
    tagged = pos_tag(word_tokenize(text))
    tree = ne_chunk(tagged)
    return tree