class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        stack, res = [], [-1] * len(A)
        num = len(A)
        for i in range(len(A*2)):
            while stack and A[stack[-1]] < A[i%num]:
                res[stack.pop()] = A[i%num]
            stack.append(i%num)
        return res
        