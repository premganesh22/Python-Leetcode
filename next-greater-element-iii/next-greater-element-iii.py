class Solution:
    
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        
        if len(set(s)) == 1:
            return -1
        
        index = len(s)-2
        while index >= 0:
            if s[index] >=s[index+1]:
                index-=1
            else:
                break
        if index < 0:
            return -1
        position = len(s)-1
        while s[index] >= s[position]:
            position-=1
        
        s[index],s[position] = s[position],s[index]
        s[index+1:] = sorted(s[index+1:])
        return int(''.join(s)) if int(''.join(s)) < 2 ** 31 else -1
            