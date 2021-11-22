class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        dic = defaultdict(int)
        for num in aliceSizes:
            dic[num] = 0
        diff = (sum(aliceSizes) - sum(bobSizes)) //2
        for num in bobSizes:
            if num+diff in dic:
                return [num+diff,num]
            
        