class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find minimum length character
        shortest = len(strs[0])
        char = strs[0]
        for i in strs:
            if shortest > len(i):
                shortest = len(i)
                char = i
            
        
        for i in range(shortest):
            for j in strs:
                if j[i] != char[i]:
                    return char[0:i]
        return char
    
        