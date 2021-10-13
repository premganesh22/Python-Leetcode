class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            
            while stack and stack[-1][0]<temperatures[i]:
                    x,y = stack.pop()
                
                    output[y] = i-y
        
            stack.append([temperatures[i],i])
        return output
            
                
            
        