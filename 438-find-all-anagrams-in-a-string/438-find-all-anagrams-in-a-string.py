class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        k = len(p)
        global_output = []
        if k > len(s):
            return []
        
        import collections
        hash_p = collections.Counter(p)

        hash_s = {}
        for i in range(k):
            hash_s[s[i]] = hash_s.get(s[i],0)+1    
        if hash_s == hash_p:
            global_output.append(i-k+1)

        for i in range(k,len(s)):
            hash_s[s[i]] = hash_s.get(s[i],0)+1   
            hash_s[s[i-k]]-=1
            if hash_s[s[i-k]] == 0:
                del hash_s[s[i-k]]
            if hash_s == hash_p:
                global_output.append(i-k+1)
        return global_output