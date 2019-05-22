import Crawler
import Trie
import rankingSearchResults

if __name__ == "__main__":  
    
    print("Welcome to the Simplified Search Engine!!")
    print("Crawling the World Wide Web...")
    
    # passing the input file containing web pages urls to the crawler
    data = Crawler.readInput("input.txt")    
    print("Crawling Successfull!")
            
    while (True):
        print("\nPlease enter the search keyword below (Enter exit to terminate): ")
        search_query = str(input())
        
        if (search_query == "exit"):
            break
            
        inputText = search_query.lower()
        splitTest = inputText.split(" ")
        trie = Crawler.getTrieObject()
        if (len(splitTest) > 1):
            search_status = []
            for x in splitTest:
                result = trie.search(x)
                search_status.append(result)
            
            if (len(search_status) == 0):
                print ("\nYour search did not match any documents: " + inputText)
            else:
                links = search_status[0] & search_status[1]
                print ("\nSearch Results \n")
                for link in links:
                    print (link)
             
        else: 
            search_status = trie.search(inputText)
            if (search_status == False):
                print ("\nYour search did not match any documents: " + inputText)
            else:
                print ("\nSearch Results \n")
                text_dict = Crawler.getTextDict()
                doc_text = []
                for link in search_status:
                    doc_text.append(text_dict.get(str(link)))
                    
                # computes TF-IDF matrix for search keyword
                ranking = rankingSearchResults.computeTFIDF(doc_text, inputText)  
                
                rank_relevance = []
                
                # retrievs the link of the documents
                for url, content in enumerate(ranking):
                    for (key, value) in text_dict.items():
                        if value == str(content[0]):
                            rank_relevance.append(key)
                            
                # displays the search results based on the TF-IDF
                for result in reversed(rank_relevance):
                    print(result)