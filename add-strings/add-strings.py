class Solution(object):
    def convert(self,nums):
        suma = 0
        i = 0
        while i < len(nums)-1:
      
            suma+= (ord(nums[i])-(ord('1')-1))
            suma*=10
            i+=1
        suma+= ord(nums[i])-(ord('1')-1)
        return suma

    def convert_int_string(self,string):
        res = ''
        while string > 9:
            res+=str(string%10)
            string//=10
        res+=str(string%10)
        return res[::-1]
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        


        sums = self.convert(num1) + self.convert(num2)
        
        return self.convert_int_string(sums)
