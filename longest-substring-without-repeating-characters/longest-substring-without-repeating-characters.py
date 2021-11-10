class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
    
    
        start = 0
        max_len = 0
        d = {}
        #abcabcbb
        #abcabcbb
        #{a,c,b} start = 5 max_len = 3
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                max_len = max(max_len, len(d))
                while char in d:
                    del d[s[start]]
                    start+=1 
                d[char] = 1
        return max(max_len,len(d))

        

    
    