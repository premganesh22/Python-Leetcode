class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        dic = {}
        for i in nums2:
            dic[i] = dic.get(i,0)+1
        output = []
        for i in nums1:
            if i in dic and dic[i] > 0:
                output.append(i)
                dic[i]-=1
        return output
        