class Solution:
    def healper(self,s):
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.healper(s) == self.healper(t)