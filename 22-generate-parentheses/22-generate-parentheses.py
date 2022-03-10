class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left,right,slate,result):
            
            if left > right:
                return
            
            if left == 0 and right == 0:
                result.append(''.join(slate[:]))
            
            else:
                if left:
                    slate.append('(')
                    helper(left-1,right,slate,result)
                    slate.pop()
                if right:
                    slate.append(')')
                    helper(left,right-1,slate,result)
                    slate.pop()
                return result
        return helper(n,n,[],[])