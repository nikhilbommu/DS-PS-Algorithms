class Solution:
    def balancedStringSplit(self, s):
        count = 0
        lc, rc = 0, 0
        for i in s:
            if i == 'R':
                lc -= 1
            else:
                lc += 1
            if lc == 0:
                count += 1
        return count

s = Solution()
print(s.balancedStringSplit("RLRRLLLR"))
