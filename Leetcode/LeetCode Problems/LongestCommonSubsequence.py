class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        for i in range(1, len(res)):
            for j in range(1, len(res[0])):
                if text1[j - 1] == text2[i - 1]:
                    res[i][j] = 1 + res[i - 1][j - 1]
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])

        return res[-1][-1]


s = Solution()
print(s.longestCommonSubsequence("abcde","abcd"))