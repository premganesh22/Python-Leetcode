class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pali(s):
            return s == s[::-1]
        
        def helper(s,idx,stack,result):
            if idx == len(s):
                result.append(stack[:])
                
            else:
                for i in range(idx,len(s)):
                    if is_pali(s[idx:i+1]):
                        stack.append(s[idx:i+1])
                        helper(s,i+1,stack,result)
                        stack.pop()
                return result
        return helper(s,0,[],[])
