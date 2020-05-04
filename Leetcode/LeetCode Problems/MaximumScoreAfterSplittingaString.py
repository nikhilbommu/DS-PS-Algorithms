class Solution:
    def maxScore(self, s) :
        maxi = -1
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            maxi = max(maxi,left.count('0')+right.count('1'))
            print(left.count('0'),right.count('1'))
        return maxi

s = Solution()
print(s.maxScore("01110"))