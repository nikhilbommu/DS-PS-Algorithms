from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        s = sorted(s)
        dct = Counter(s)
        length = len(dct)
        result = ""
        i = 0
        loop = 0
        while i < len(s):
            temp = ""
            for j in dct:
                if dct[j] > 0:
                    temp += j
                    dct[j] -= 1
                    i += 1
            if loop % 2 == 0:
                result += temp
            else:
                result += temp[::-1]
            loop += 1

        return result

s = Solution()
print(s.sortString("leetcode"))