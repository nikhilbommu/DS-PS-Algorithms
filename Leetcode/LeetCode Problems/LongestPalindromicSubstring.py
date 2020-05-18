class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(set(s)) == 1 or s == s[::-1]:
            return s
        res = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(res) :
                    res = s[i:j+1]
        return res

s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))