class Solution:
    def evalRPN(self, arr: List[str]) -> int:
        stack = []
        for i in arr:
            if i not in '+-/*':
                stack.append(int(i))
            else:
                l,r = stack.pop(), stack.pop()
              
                if i == '+':
                    stack.append(r+l)
                elif i == '-':
                    stack.append(r-l)
                elif i == '*':
                    stack.append(r*l)
                elif i == '/':
                    stack.append(int(r/l))
        return stack.pop()