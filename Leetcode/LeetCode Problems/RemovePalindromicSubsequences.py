class Solution:
    def removePalindromeSub(self, s):
        if s == "":
            return 0
        elif s == s[::-1]:
            return 1
        return 2

s = Solution()
print(s.removePalindromeSub("aabb"))