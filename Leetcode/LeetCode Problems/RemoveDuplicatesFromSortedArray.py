class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]

            else:
                i += 1
        return len(nums)

s = Solution()
print(s.removeDuplicates([1,1,2,3,3,4]))