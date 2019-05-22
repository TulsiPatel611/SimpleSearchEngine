# A simplified Search Engine

The project implements a simple Search Engine in Python. The web crawler crawls the links provided in the input file and scrapes the content of these web pages. The scraped content is then processed into tokens (index terms) by excluding the stop words.

The index terms are stored in the Trie data structure along with the URL at which the word is encountered. A set of URLs is stored at each character level or node. After the successful insertion of index terms in the Trie, the crawling is notified as being completed successfully. 

The user is then requested to give an input and the engine searches for the index term in the Trie. If the match is found then the resulting URLs are displayed as the search results. The search engine implemented here can search for one-word to long tail keywords.

Ranking Function:

A simple ranking function is implemented using the TF-IDF matrix. TF-IDF is composed by two terms:
•	TF (Term Frequency): which measures how frequently a term, say w, occurs in a document.
•	IDF (Inverse Document Frequency): measures how important a term is within the corpus (set of documents).

The ranking function implemented here computes the TF-IDF weight for the query term in the set of documents it has appeared. The TF-IDF weights are then sorted in descending order and the search result is displayed to the user.
