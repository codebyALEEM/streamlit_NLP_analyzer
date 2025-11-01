import pickle
import nlp_functions as nf

nlp_dict = {
    'tokenize' : nf.tokenize,
    'stem' : nf.stem,
    'lemmatize' : nf.lemmatize,
    'pos' : nf.pos,
    'ner' : nf.ner
}

with open("nlp_functions.pkl",'wb') as f:
    pickle.dump(nlp_dict,f)