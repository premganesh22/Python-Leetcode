class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        output = []
        l,r=0,0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                if not output or output[-1] != nums1[l]:
                    output.append(nums1[l])
                 
                l+=1
                r+=1
            elif nums1[l] < nums2[r]:
                l+=1
            else:
                r+=1
        return output
        