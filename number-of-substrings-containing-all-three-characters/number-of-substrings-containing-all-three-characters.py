class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start = 0
        count = 3
        output = 0
        dic = {'a':1,'b':1,'c':1}
        for end in range(len(s)):
            if s[end] in dic:
                if dic[s[end]] > 0:
                    count-=1
                dic[s[end]]-=1

            while count==0:
                output+=len(s)-end
                if s[start] in dic:
                    dic[s[start]]+=1
                    if dic[s[start]] > 0:
                        count+=1
                start+=1
        return output
        