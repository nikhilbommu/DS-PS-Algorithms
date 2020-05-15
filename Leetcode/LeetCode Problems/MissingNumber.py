class Solution:
    def missingNumber(self, nums) -> int:
        actual_sum = (len(nums) * (len(nums) + 1)) // 2
        return actual_sum - sum(nums)

s = Solution()
print(s.missingNumber([3,0,1]))