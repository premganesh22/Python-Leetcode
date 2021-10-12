class Solution:
    #https://www.youtube.com/watch?v=2EErQ25kKE8
    def calculate(self, arr: str) -> int:
        stack = []
        all_operators = ['+','-','*','/']
        cur_num = 0
        operator = '+'
        nums = set(str(a) for a in range(10))
        for i in range(len(arr)):
            char = arr[i]

            if char in nums:
                cur_num=cur_num*10+int(char)
                
            if char in all_operators or i == len(arr)-1:
                if operator == '+':
                    
                    stack.append(cur_num)
                    
                elif operator == '-':
                    stack.append(-cur_num)
                elif operator == '*':
                    stack[-1] = stack[-1]*cur_num
                else:
                    print(stack)
                    stack[-1] = int(stack[-1]/cur_num)
                cur_num = 0
                operator = char
        return sum(stack)