class Solution:
    def calculate(self, s: str) -> int:
        def helper(s,pointer):
            output = []  
            nums = '0123456789'
            num = 0
            sign = '+'

            def update():
                if sign == '+':
                    output.append(num)
                elif sign == '-':
                    output.append(-num)
                elif sign == '*':
                    output.append(output.pop()*num)
                else:
                    output.append(int(output.pop()/num))

            while pointer < len(s):

                if s[pointer] in nums:
                    num = num*10 + int(s[pointer])

                elif s[pointer] in ['+','-','/','*']:
                    update()
                    sign = s[pointer]
                    num = 0
                elif s[pointer] == '(':
                    num,pointer = helper(s,pointer+1)
                elif s[pointer] == ')':
                    update()
                    return sum(output),pointer
                pointer+=1
            return sum(output)
        s+='+'
        return helper(s,0)
        