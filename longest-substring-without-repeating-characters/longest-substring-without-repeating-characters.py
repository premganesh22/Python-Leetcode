class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_sum = 0
        lista = {}
        for end in range(len(s)):
            if s[end] not in lista:
                lista[s[end]] = 1
            else:
                max_sum = max(max_sum,len(lista))
                while s[end] != s[start]:
                    del lista[s[start]]
                    start+=1
                start+=1
                #del lista[s[left]]
        return max(max_sum,len(lista))
        