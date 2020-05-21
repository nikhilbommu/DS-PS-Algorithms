class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        start = 0
        word = ""
        while start < len(s):
            if s[start] not in word:
                word += s[start]
            else:
                if len(word) > maxi:
                    maxi = len(word)
                start = start - len(word)
                word = ""
            start += 1
        if len(word) > maxi:
            maxi = len(word)
        return maxi

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))