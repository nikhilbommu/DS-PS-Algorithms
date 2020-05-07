class Solution:
    def generateTheString(self, n) :
        words = "xy"
        if n%2 != 0:
            return words[0]*n
        else:
            return words[0]*(n-1) + words[1]*1

s = Solution()
print(s.generateTheString(4))