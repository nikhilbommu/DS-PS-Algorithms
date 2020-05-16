class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        i = 0
        word = ""
        while i<len(s)-1:
            word += s[i]
            temp = length // len(word)
            if word * temp == s:
                return True
            i += 1
        return False

s = Solution()
print(s.repeatedSubstringPattern("aba"))
print(s.repeatedSubstringPattern("abcabcabcabc"))