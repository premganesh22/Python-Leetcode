class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates,target,slate,result):
            total = sum(slate)
            if total == target:
                result.append(slate[:])
                return
            elif total > target or len(candidates) == 0:
                return
            else:
                #Include
                count = 0
                cur_num = candidates[0]
                for i in range(len(candidates)):
                    if cur_num == candidates[i]:
                        count+=1
                for i in range(count):
                    slate.append(candidates[i])
                    helper(candidates[count:],target,slate,result)
                for i in range(count):
                    slate.pop()
                    
                #Exclude
                helper(candidates[count:],target,slate,result)
                return result
        
        return helper(sorted(candidates),target,[],[])
        