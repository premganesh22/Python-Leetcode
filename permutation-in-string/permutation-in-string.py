class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maps = defaultdict(int)
        for i in s1:
            maps[i]+=1
        length = len(s1)
        start = 0
        counter = 0
        
        for end in range(len(s2)):
            if maps[s2[end]] > 0:
                counter+=1
            maps[s2[end]]-=1
            while counter == length:
                print(end,start)
                if end-start+1 == length:
                    return True
                maps[s2[start]]+=1
                if maps[s2[start]]>0:
                    counter-=1
                start+=1
        return False
            
        