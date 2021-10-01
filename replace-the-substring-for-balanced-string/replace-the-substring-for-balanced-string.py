class Solution:
    def balancedString(self, s: str) -> int:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        extra = {}
        for key,value in dic.items():
            if value > len(s)//4:
                extra[key] = value - (len(s)//4)
        if not extra:
            return 0
        start = 0
        minlen = len(s)
        for end in range(len(s)):
            if s[end] in extra:
                extra[s[end]]-=1
            #print(extra)
            while max(extra.values()) <= 0:

                minlen = min(end-start+1,minlen)
                if s[start] in extra:
                    extra[s[start]]+=1
                start+=1
        return minlen
        