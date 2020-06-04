class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        result = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(result)):
            result[i][i] = 1

        for l in range(2, len(result) + 1):
            for i in range(len(result) - l + 1):
                j = l + i - 1
                if s[i] == s[j]:
                    result[i][j] = 2 + result[i + 1][j - 1]
                else:
                    result[i][j] = max(result[i][j - 1], result[i + 1][j])

        return result[0][-1]

s= Solution()
print(s.longestPalindromeSubseq("bbbab"))