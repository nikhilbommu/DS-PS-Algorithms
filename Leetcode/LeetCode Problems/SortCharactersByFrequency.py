from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dct = Counter(s)
        result = ""

        for k, v in sorted(dct.items(), key=lambda s: (s[1], s[0]), reverse=True):
            result += k * v

        return result

s = Solution()
print(s.frequencySort("tree"))