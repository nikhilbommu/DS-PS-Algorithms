class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if Counter(s) == Counter(t):
            return True
        return False"""

        if len(s) == len(t):
            for char in set(s):
                if s.count(char) != t.count(char):
                    return False
            return True
        else:
            return False

s = Solution()
print(s.isAnagram("anagram","nagaram"))