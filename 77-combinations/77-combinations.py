class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def nk(cur_num,n,k,slate,result):
            if k == 0:
                result.append(slate[:])
                return result
            if cur_num > n:
                return 
            else:
                #Include
                slate.append(cur_num)
                nk(cur_num+1,n,k-1,slate,result)
                slate.pop()

                #Exclude
                nk(cur_num+1,n,k,slate,result)
                return result

        return nk(1,n,k,[],[])
