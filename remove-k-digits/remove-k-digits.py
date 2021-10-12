class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        count = 0
        stack = [num[0]]
        for i in range(1,len(num)):

            if count == k:

                stack.extend(num[i:])
                break
            else:
                while stack and stack[-1] > num[i] and count <k:
                    stack.pop()
                    count+=1
                stack.append(num[i])
        n = len(stack) - (k-count)
        return str(int(''.join(stack[:n])))
        