class TrieNode(object):
    def __init__(self):
        
        # Initializing the trie data structure here.
        
        self.isEnd = False  # whether this node is an end of a word
        self.children = dict()  # map a char to the child node
        self.url = set() # set of url strings where the character is found

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, url):

        # Inserts a word into the trie.
        
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
                currNode.children[c].url.add(url)
               
            currNode = currNode.children[c]
            currNode.url.add(url)
        currNode.isEnd = True

    def search(self, word):
        
        # Search for a word or character in the trie.
        # Returns the url (web page link) consisting of that word or character in it's text, if the word is in the trie.
        
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]

        return currNode.url

    def startsWith(self, prefix):
        
        # Prefix search - Returns if there is any word in the trie that starts with the given prefix.
        
        currNode = self.root

        for c in prefix:
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]

        return True
