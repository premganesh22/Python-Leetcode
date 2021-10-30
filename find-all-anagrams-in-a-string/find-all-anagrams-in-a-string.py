class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = defaultdict(int)
        for i in p:
            dic[i]+=1
        
        start = 0
        counter = len(p)
        output = []
        
        for end in range(len(s)):
            
            if dic[s[end]] > 0:
                counter-=1
            dic[s[end]]-=1
            
            while counter == 0:
                if end-start+1 == len(p):
                    output.append(start)
                
                dic[s[start]]+=1
                if dic[s[start]] > 0:
                    counter+=1
                start+=1
        return output