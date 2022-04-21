class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = []
        for temp in reversed(range(len(temperatures))):
            while stack and stack[-1][0] <= temperatures[temp]:
                stack.pop()
            if stack:
                output.append(stack[-1][1]-temp)
            else:
                output.append(0)
            stack.append((temperatures[temp],temp))
        return output[::-1]
        