class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            while stack and aster < 0 and stack[-1] > 0:
                if abs(aster) == stack[-1]:
                    stack.pop()
                    break
                elif abs(aster) > stack[-1]:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(aster)
        return stack