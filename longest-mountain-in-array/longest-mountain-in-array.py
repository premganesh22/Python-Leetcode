class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        output = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = i-1
                r = i+1
                while 0 < l and arr[l] > arr[l-1]:
                    l-=1

                while len(arr)-1 > r and arr[r] > arr[r+1]:
                    r+=1
                output = max(output,r-l+1)
        return output
        