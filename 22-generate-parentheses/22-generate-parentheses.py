class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def paren(left,right,slate,result):
            #Back tracking
            if right < left:
                return
            elif right == 0 and left == 0:
                result.append(''.join(slate))
                return
            else:
                #add left
                if left > 0:
                    slate.append('(')
                    paren(left-1,right,slate,result)
                    slate.pop()
                if right > 0:
                    slate.append(')')
                    paren(left,right-1,slate,result)
                    slate.pop()
                return result
        return paren(n,n,[],[])
