class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            while stack and i < 0 and stack[-1] > 0:
                if stack[-1] == abs(i):
                    stack.pop()
                    break
                elif stack[-1] > abs(i):
                    break
                elif stack[-1] < abs(i):
                    stack.pop()
                    continue
            else:
                stack.append(i)
        return stack