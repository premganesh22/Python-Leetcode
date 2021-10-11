class Solution:
    #https://www.youtube.com/watch?v=Ya-LfQ0OBkU
    def candy(self, arr: List[int]) -> int:
        left = [1]*len(arr)
        right = [1]*len(arr)

        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                left[i] = left[i-1]+1
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1] < arr[i]:
                right[i] = right[i+1]+1
        res = 0
        for i in range(len(left)):
            res+=max(left[i],right[i])
        return res
        