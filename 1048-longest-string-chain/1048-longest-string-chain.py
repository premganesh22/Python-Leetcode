class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        word_map = {}
        max_val = 1
        for word in sorted(words, key=len):
            word_map[word] = 1
            
            for i in range(len(word)):
                val = word[:i] + word[i+1:]
                if val in word_map:
                    word_map[word] = max(word_map[word], word_map[val]+1)
                    max_val = max(max_val, word_map[word])
                    
        return max_val