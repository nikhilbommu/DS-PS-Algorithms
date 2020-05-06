from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        c = Counter(nums)
        for i in sorted(c):
            if c[i] > len(nums) // 2:
                return i

        seen = set(nums)
        for i in seen:
            if nums.count(i) > len(nums) // 2:
                return i
s = Solution()
print(s.majorityElement([2,3,2]))