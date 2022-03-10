class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates,target,slate,result):
            
            if sum(slate) == target:
                result.append(slate[:])
                return 
            if sum(slate) > target:
                return
            
            if len(candidates) == 0:
                return
            cur_num = candidates[0]
            count=0
            for i in range(len(candidates)):
                if candidates[i] == cur_num:
                    count+=1
            #Include
            for i in range(count):
                slate.append(candidates[i])
                helper(candidates[count:],target,slate,result)
            
            for i in range(count):
                slate.pop()
            
            #Exclude
            helper(candidates[count:],target,slate,result)
            return result
        return helper(sorted(candidates),target,[],[])