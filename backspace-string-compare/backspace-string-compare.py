class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def clean(s):
            #'ab#'
            #"bxj##tw"
            #  "bxj###tw"
            pointer = len(s)-1 #6
            out = '' 
            count = 0
            while pointer >= 0: #2 1
                if s[pointer] == '#': #5 c = 0  4, 0; 3,1, 2,2, 1,11,, 0, 0 wtb wt
                    count+=1
                elif count:
                    count-=1
                else:
                    out+=s[pointer]
                pointer-=1
            return out

        return clean(s) == clean(t)
    
    
        