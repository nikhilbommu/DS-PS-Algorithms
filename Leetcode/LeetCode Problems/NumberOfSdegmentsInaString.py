class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)):
            if (i == 0 or s[i-1] == " ") and s[i] != " ":
                count += 1
        return count

s = Solution()
print(s.countSegments("Hello, have a nice day"))