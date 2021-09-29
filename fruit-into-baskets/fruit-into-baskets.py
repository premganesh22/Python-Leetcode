class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0,0
        max_sum = 0
        dic = {}
        while end < len(fruits):
            if fruits[end] in dic or len(dic)<2:
                dic[fruits[end]] = dic.get(fruits[end],0)+1
                end+=1
            else:
                max_sum = max(max_sum,sum(dic.values()))
                dic[fruits[start]]-=1
                if dic[fruits[start]] == 0:
                    del dic[fruits[start]]
                start+=1
        max_sum = max(max_sum,sum(dic.values()))

        return max_sum
        