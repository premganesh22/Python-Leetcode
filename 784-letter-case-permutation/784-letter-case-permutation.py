class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        output = []
        def helper(string, slate):
            if len(slate) == len(s):
                output.append(''.join(slate))
            for i in range(len(string)):
                
                if string[i].isdigit():
                    slate.append(string[i])
                    helper(string[i+1:], slate)
                    slate.pop()
                    
                else:
                    
                    slate.append(string[i].upper())
                    helper(string[i+1:], slate)
                    slate.pop()

                    slate.append(string[i].lower())
                    helper(string[i+1:], slate)
                    slate.pop()
                
        helper(s, [])
        return output
                
        