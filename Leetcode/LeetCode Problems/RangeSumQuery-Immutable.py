class NumArray:

    def __init__(self, nums: List[int]):
        self.lst = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.lst[i+1] = self.lst[i] + nums[i]
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.lst[j+1]
        return self.lst[j+1] - self.lst[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)