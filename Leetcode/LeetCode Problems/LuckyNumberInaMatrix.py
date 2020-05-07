class Solution:
    def luckyNumbers(self, matrix):
        mini = set()
        for i in range(len(matrix)):
            mini.add(min(matrix[i]))
        maxi = set()
        for c in zip(*matrix):
            maxi.add(max(c))

        return mini.intersection(maxi)

s = Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))