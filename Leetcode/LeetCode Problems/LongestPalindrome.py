from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = Counter(s)
        length = 0
        for val in dict.values():
            length += (val//2)*2
        if length == len(s):
            return length
        else:
            return length+1

s = Solution()
print(s.longestPalindrome("abccccdd"))