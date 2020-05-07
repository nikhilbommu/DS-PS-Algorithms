class Solution:
    def minSubsequence(self, nums):
        if len(nums) == 1:
            return nums
        nums = sorted(nums)
        i = len(nums)-1
        while i>0:
            if sum(nums[i:]) > sum(nums[:i]):
                return nums[i:][::-1]
            elif sum(nums[i:]) == sum(nums[:i]):
                return nums[i-1:][::-1]
            i-=1

s = Solution()
print(s.minSubsequence([4,6,7,7,6]))