import nltk as np

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def computeTFIDF(doc_text, keyword):
    
    # computes a term frequence - inverse document frequency matrix for the documents (links) returned by the search in the trie.
    # NOTE: each web page is referred to as a document.
    # ** TF-IDF**: is composed by two terms:
    # TF(Term Frequency): which measures how frequently a term, say w, occurs in a document.
    # IDF (Inverse Document Frequency): measures how important a term is within the corpus (set of document).
    # The ranking function implemented here computes the TF-IDF weight for the query term in the set of documents it has appeared.
    # The TF-IDF weights are then sorted descending order and matched with the document it belongs to.

    tfidf_vect = TfidfVectorizer() 
    tfidf_vect = TfidfVectorizer(stop_words="english") 

    # generate tfidf matrix
    dtm = tfidf_vect.fit_transform(doc_text)
    # print (dtm)
    # print("type of dtm:", type(dtm))
    # print("size of tfidf matrix:", dtm.shape)
    # print(tfidf_vect.get_feature_names())
    
    tfidf_weights = {x:dtm[idx, tfidf_vect.vocabulary_[keyword]] for idx, x in enumerate(doc_text)}
    # print(tfidf_weights)
    
    return (sorted(tfidf_weights.items(), key = lambda kv:(kv[1], kv[0])))       
        
