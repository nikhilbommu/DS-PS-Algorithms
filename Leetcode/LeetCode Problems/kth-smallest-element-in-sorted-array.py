from heapq import heappush,heappop
class Solution:
    def kthSmallest(matrix,k):
        mat=[]
        res = 0
        for r in matrix:
            for e in r:
                heappush(mat, e)
        for i in range(k):
            res = heappop(mat)
        return res
s=Solution
print(s.kthSmallest([[4,5,6],[7,8,9],[1,2,3]],8))