class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for num in asteroids:
            while stack and num < 0 and stack[-1] > 0:
                if stack[-1] == abs(num):
                    stack.pop()
                    break
                elif stack[-1] < abs(num):
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(num)

        return stack
        