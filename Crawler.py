import requests
import urllib.request
import nltk
import string
import Trie

from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.corpus import stopwords

string.punctuation

# instance of trie object
trie = Trie.Trie()
text_dict = {}

def visibleTags(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def dataScraping(body):
    
    # scrapes the web pages provided in the input.txt file
    # Returns the scraped text content.
    
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text = True)
    visible_texts = filter(visibleTags, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def tokenization(document, url):
    
    # tokenizes the input documents
    tokens = nltk.word_tokenize(document.lower()) 

    # removes punctuations
    tokens = [token.strip(string.punctuation) for token in tokens]
    
    # removes empty tokens
    tokens = [token.strip() for token in tokens if token.strip() != '']
        
    # word frequency distribution
    word_dist = nltk.FreqDist(tokens)
    
    # removes stop words
    stop_words = stopwords.words('english')
    stop_words += ["»", "“", "”", "©", "’", "📩", "✨", "🎧"]
    
    # dictionary of words (keys) and it's word count (value)
    filtered_dict = {word: word_dist[word] for word in word_dist if word not in stop_words}
    # print (filtered_dict)

    for key in filtered_dict:
        trie.insert(key, url)   # inserting words into the trie data structure
    # print("Trie Insertion Successfull!!")
    
def getTrieObject():   # returns trie object
    return trie

def getTextDict():
    return text_dict
    
def readInput(input):
    
    # Reads input.txt file line by line and passes the url to dataScraping method to get the text out of the html.
    # The text after data processing is inputed to the tokenization method along with the url to insert it into the trie.
    
    input_file = open(input,"r")
    
    for url in input_file:
        html = urllib.request.urlopen(url)
        text = dataScraping(html)
        url = url.rstrip()
        if url not in text_dict:
            text_dict[url] = str(text).lower()
        tokens = tokenization(text, url)
        
    input_file.close()
