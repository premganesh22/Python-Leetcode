class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        dic = {}
        for i in aliceSizes:
            dic[i] = 1

        difference = int((sum(aliceSizes) - sum(bobSizes)) / 2)
        for i in bobSizes:
            if difference+i in dic:
                return [difference+i,i]