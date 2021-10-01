class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        for i in t:
            dic[i]+=1
        start = 0
        minstart = 0
        minlen = len(s)+1
        counter = len(t)
        for end in range(len(s)):

            if dic[s[end]] > 0:
                counter-=1
            dic[s[end]]-=1

            while counter == 0:
                if minlen > end-start+1:
                    minlen = end-start+1
                    minstart = start
                dic[s[start]]+=1
                if dic[s[start]] > 0:
                    counter+=1
                start+=1
        if minlen == len(s)+1:
            return ""
        return s[minstart:minstart+minlen]