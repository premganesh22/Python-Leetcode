class Solution:
    def decodeString(self, string: str) -> str:
        stack = [['','1']]
        curnum = 0
        char = ''
        for i in string:
            
            if i.isdigit():
                curnum = curnum*10 + int(i)
            elif i == '[':
                stack.append(['',curnum])
                curnum = 0
            elif i == ']':
                string, k = stack.pop()
                stack[-1][0]+=string*k
            else:
                stack[-1][0]+= i
        return stack[0][0]
        