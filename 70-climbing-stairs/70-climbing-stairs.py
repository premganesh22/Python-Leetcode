class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        output = [0]*(n+1)
        output[1] = 1
        output[2] = 2
        for num in range(3,n+1):
            output[num] = output[num-1]+output[num-2]
        return output[n]