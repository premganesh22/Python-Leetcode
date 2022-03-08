class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def queen(n,idx,slate,result):

            #Backtracking
            last_idx = idx-1
            if last_idx > 0:
                for each_idx in range(last_idx):
                    if slate[each_idx] == slate[last_idx]:
                        return
                    elif abs(last_idx-each_idx) == abs(slate[each_idx]- slate[last_idx]):
                        return

            #Base Case
            if idx == n:

                temp = []
                for i in slate:
                    a = []
                    for j in range(n):
                        if j == i:
                            a.append('Q')
                        else:
                            a.append('.')

                    temp.append("".join(a))
                result.append(temp[:])
                return

            #Logic
            for col in range(0,n):
                slate.append(col)
                queen(n,idx+1,slate,result)
                slate.pop()
            return result
        
        return queen(n,0,[],[])