class Solution:
    def calculate(self, s: str) -> int:
        s += "+"
        output = []
        pointer = 0
        nums = '0123456789'
        num = 0
        sign = '+'
        while pointer < len(s):

            if s[pointer] in nums:
                num = num*10 + int(s[pointer])

            elif s[pointer] in ['+','-','/','*']:
                if sign == '+':
                    output.append(num)
                elif sign == '-':
                    output.append(-num)
                elif sign == '*':
                    output.append(output.pop()*num)
                else:
                    output.append(int(output.pop()/num))
                sign = s[pointer]
                num = 0
            pointer+=1
        return sum(output)
        