class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_sum = 0 
        while left < right:
            minimum = min(height[left],height[right])
            max_sum = max(max_sum,minimum*(right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_sum
        