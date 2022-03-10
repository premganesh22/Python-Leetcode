class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(n,cur_num,k,slate,result):

            if k == 0:
                result.append(slate[:])
                return result
            if cur_num > n:
                return
            else:
                #Exlcude
                helper(n,cur_num+1,k,slate,result)
                
                #Include
                slate.append(cur_num)
                helper(n,cur_num+1,k-1,slate,result)
                slate.pop()
            return result
        return helper(n,1,k,[],[])