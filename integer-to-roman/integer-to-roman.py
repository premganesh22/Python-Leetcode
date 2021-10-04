class Solution:
    def intToRoman(self, num: int) -> str:
        strings= ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
        
        res = ''
        i=0
        while i < len(nums):
            if num >= nums[i]:
                num-=nums[i]
                res+=strings[i]
                pass
            else:
                i+=1
        return res
        