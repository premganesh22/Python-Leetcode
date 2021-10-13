class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = [nums2[0]]
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        output = []
        for i in nums1:
            if i in dic:
                output.append(dic[i])
            else:
                output.append(-1)
        return output