class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curNode = self.root
        for letter in word:
            if not letter in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for letter in word:
            if not letter in curNode.children:
                return False
            curNode = curNode.children[letter]
        return curNode.end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for letter in prefix:
            if not letter in curNode.children:
                return False
            curNode = curNode.children[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)