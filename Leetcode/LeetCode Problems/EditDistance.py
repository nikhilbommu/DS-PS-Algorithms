class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        result = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        for i in range(len(result[0])):
            result[0][i] = i
        for i in range(len(result)):
            result[i][0] = i
        for i in range(1, len(result)):
            for j in range(1, len(result[0])):
                if word1[j - 1] == word2[i - 1]:
                    result[i][j] = result[i - 1][j - 1]
                else:
                    result[i][j] = 1 + min(result[i - 1][j], result[i][j - 1], result[i - 1][j - 1])

        return result[-1][-1]

s = Solution()
print(s.minDistance("intention","execution"))