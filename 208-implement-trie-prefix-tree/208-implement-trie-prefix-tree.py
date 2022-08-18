class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur_word = self.root
        
        for char in word:
            if char not in cur_word.children:
                cur_word.children[char] = TrieNode()
                
            cur_word = cur_word.children[char]
        cur_word.end_of_word = True

    def search(self, word: str) -> bool:
        cur_word = self.root
        for char in word:
            if char not in cur_word.children:
                return False
            cur_word = cur_word.children[char]
        
        return cur_word.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur_word = self.root
        for char in prefix:
            if char not in cur_word.children:
                return False
            cur_word = cur_word.children[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)