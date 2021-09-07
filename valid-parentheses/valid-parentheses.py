class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = ['(','[','{']
        closed = [')',']','}']
        stack = []
        for c in s:
            
            if c in opened:
                stack.append(c)
            else:
                if stack and stack[-1] == opened[closed.index(c)]: 
                    stack.pop()
                else:
                    return False
        print("hi")
        print(stack)
        return False if stack else True
        