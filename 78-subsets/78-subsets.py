class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(s,slate,result):
            if len(s) == 0:
                result.append(slate.copy())
                return result
            else:
                #Include
                slate.append(s[0])
                sub(s[1:],slate,result)
                slate.pop()

                #Exlcude
                sub(s[1:],slate,result)
                return result
        return sub(nums,[],[])
        