class Solution:
    def createTargetArray(self, nums, index):
        lst = [0] * len(nums)
        for i in range(len(nums)):
            lst.insert(index[i], nums[i])
        return lst[:len(nums)]

s = Solution()
print(s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))