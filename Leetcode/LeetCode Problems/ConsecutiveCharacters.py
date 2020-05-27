class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count = 1
        maxi = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                count = 1
            maxi = max(count, maxi)
        return maxi

s = Solution()
print(s.maxPower("leetcode"))