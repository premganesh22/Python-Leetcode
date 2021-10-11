class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char]+=1
        
        freq = sorted(freq.items(), key=lambda x:x[1])[::-1]
        
        res = ''
        for i in freq:
            res+=i[0]*i[1]
        return res
            
            
            
        
        