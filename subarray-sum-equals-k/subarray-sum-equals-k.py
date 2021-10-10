class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        count=0
        dic[0] = 1
        suma = 0
        for i in nums:
            suma+=i
            count+=dic[suma-k]
            dic[suma]+=1
        return count