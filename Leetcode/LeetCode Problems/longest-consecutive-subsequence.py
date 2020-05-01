class Solution:
    def longestConsecutive(nums) -> int:
        nums = list((sorted(set(nums))))
        c = 1
        maxi = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                c += 1
            else:
                c = 1
            maxi = max(maxi, c)
        return maxi
s=Solution
print(s.longestConsecutive([0, 1, 2, 3, -1, -3]))