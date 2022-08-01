class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        result = [-1]*(n+1)
        
        result[0] = 1
        result[1] = 1
        
        if n <2:
            return result[n]
        
        for i in range(2,n+1):
            result[i] = result[i-1] + result[i-2]
            
        return result[-1]
        