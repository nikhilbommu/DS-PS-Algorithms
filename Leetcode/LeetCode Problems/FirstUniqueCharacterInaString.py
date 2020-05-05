from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        c = Counter(s)
        for index,value in enumerate(s):
            if c[value] == 1:
                return index
        return -1
        """
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1"""

s = Solution()
print(s.firstUniqChar("nikhil"))