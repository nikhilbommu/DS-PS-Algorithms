class Solution:
    def findRelativeRanks(self, nums):
        lst = sorted(nums, reverse=True)
        for i in range(len(lst)):
            ind = nums.index(lst[i])
            if i == 0:
                nums[ind] = "Gold Medal"
            elif i == 1:
                nums[ind] = "Silver Medal"
            elif i == 2:
                nums[ind] = "Bronze Medal"
            else:
                nums[ind] = str(i + 1)
        return nums

s = Solution()
print(s.findRelativeRanks([5,4,3,2,1]))
print(s.findRelativeRanks([10,3,9,8,4]))