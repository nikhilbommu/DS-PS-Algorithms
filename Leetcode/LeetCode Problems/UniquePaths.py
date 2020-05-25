class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1 for i in range(m)] for j in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]

s = Solution()
print(s.uniquePaths(3,2))
print(s.uniquePaths(7,3))
print(s.uniquePaths(3,3))