class Solution(object):        
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        count = 1
        index = 0
        for i in range(1,len(chars)+1):
            if i < len(chars) and chars[i] == chars[i-1]:
                count+=1
            else:
                chars[index] = chars[i-1]
                index+=1
                if count > 1:
                    for j in str(count): 
                        chars[index] = j
                        index+=1
                count = 1
        return index