class Solution:
    def generate(numRows: int):
        c = []
        l = [[1], [1, 1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return l
        else:
            for i in range(2, numRows):
                tem = [1] * (i + 1)
                for j in range(1, i):
                    tem[j] = l[i - 1][j - 1] + l[i - 1][j]
                l.append(tem)
            return l
    print(generate(5))