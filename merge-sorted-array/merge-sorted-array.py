class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
   
        while n > 0 and m > 0:
            if nums1[m-1] <= nums2[n-1]: #3 < 6; 3 < 5
                nums1[ m+n-1] = nums2[n-1] #5:6; 4:5
                n-=1 #n2 n1
                
            else:
                nums1[m+n-1] = nums1[m-1]
                m-=1

        while n > 0:
            nums1[m+n-1] = nums2[n-1]
            n-=1
        