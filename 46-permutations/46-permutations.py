class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def per(s,slate,result):
            if len(s) == 0:
                result.append(slate.copy())
            else:
                for i in range(len(s)):
                    slate.append(s[i])
                    per(s[:i]+s[i+1:],slate,result)
                    slate.pop()
                return result
        return per(nums,[],[])

                