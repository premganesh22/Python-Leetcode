class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = 0
        self.prefix_array = [0]
        for num in nums:
            self.prefix_sum+=num
            self.prefix_array.append(self.prefix_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_array[right+1]-self.prefix_array[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)