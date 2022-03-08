class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(candidates,target,slate,result):
            if sum(slate) == target:
                result.append(slate[:])
                return
            
            elif sum(slate) > target:
                return
            
            else:
                for num in range(len(candidates)):
                    slate.append(candidates[num])
                    helper(candidates[num:],target,slate,result)
                    slate.pop()
                return result
                
        return helper(candidates,target,[],[])