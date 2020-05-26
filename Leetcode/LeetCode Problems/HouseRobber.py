class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp)

s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,1,1,2]))