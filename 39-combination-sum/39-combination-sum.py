class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates,idx,target,slate,result):
            if sum(slate) == target:
                result.append(slate[:])
                return
            
            if sum(slate) > target or len(candidates) == 0:
                return
            
            for i in range(idx,len(candidates)):
                slate.append(candidates[i])
                helper(candidates,i,target,slate,result)
                slate.pop()
            return result
        return helper(candidates,0,target,[],[])
                
                
        
