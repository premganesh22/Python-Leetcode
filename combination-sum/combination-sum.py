class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            
        output = []
        
        
        def helper(candidates, target,path,output):
            
            if target < 0:
                return
                
            if target == 0:
                output.append(path)
                return 
            
            for num in range(len(candidates)):
                new_target = target-candidates[num]
                helper(candidates[num:],new_target,path+[candidates[num]],output)
                
        helper(candidates, target,[],output)    
        return output
        
        
        