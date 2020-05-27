class Solution:
    def sortedSquares(self, A):
        res = [0] * len(A)
        start = 0
        end = len(A) - 1
        i = end
        while start <= end:
            square1 = A[start] * A[start]
            square2 = A[end] * A[end]
            if square1 > square2:
                res[i] = square1
                start += 1
            else:
                res[i] = square2
                end -= 1
            i -= 1

        return res

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))