class Solution:
    def thirdMax(self, nums) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return max(nums)
        count = 0
        for i in nums[::-1]:
            if count == 2:
                return i
            count += 1

s = Solution()
print(s.thirdMax([3,2,1]))
print(s.thirdMax([3,2,1,4,5,6]))

