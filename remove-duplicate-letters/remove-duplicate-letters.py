class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {char:index for index,char in enumerate(s)}
        stack = []
        for i,char in enumerate(s):
            if char not in stack:
                while stack and stack[-1] > char and dic[stack[-1]] > i:
                    stack.pop()
                stack.append(char)
        return ''.join(stack)