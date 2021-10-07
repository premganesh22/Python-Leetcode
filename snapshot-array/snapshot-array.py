class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.arr = [[[-1,0]] for i in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.arr[index].append([self.snap_id,val])
        

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id+=1
   
        
        return self.snap_id-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        arr = self.arr[index]
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans == -1: return 0
        return arr[ans][1]
    
#         for i in self.arr[index][::-1]:
#             if snap_id > i[0]:
#                 return i[1]
#             if i[0] == snap_id:
#                 return i[1]
            
#         return 0

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)