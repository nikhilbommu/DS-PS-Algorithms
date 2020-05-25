class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        res = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        for i in range(1, len(res)):
            for j in range(1, len(res[0])):
                if A[j - 1] == B[i - 1]:

                    res[i][j] = 1 + res[i - 1][j - 1]
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])

        return res[-1][-1]

s = Solution()
print(s.maxUncrossedLines([1,4,2],[1,2,4]))