class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        hashmap = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1]<num:
                stack.pop()
            if stack:
                hashmap[num] = stack[-1]
            stack.append(num)
        
        return [hashmap[num] if num in hashmap else -1 for num in nums1 ]