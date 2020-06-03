from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i] :
                    result[i] = max(result[i] , result[j] + 1)
        return max(result)

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))