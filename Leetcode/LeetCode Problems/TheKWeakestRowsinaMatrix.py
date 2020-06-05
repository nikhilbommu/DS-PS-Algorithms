from typing import List
from operator import itemgetter

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dct = {}
        start = 0
        result = []
        for i in mat:
            if 0 in i:
                dct[start] = i.index(0)
            else:
                dct[start] = len(mat[0])
            start += 1
        d = sorted(dct.items(), key=itemgetter(1))
        for i in range(k):
            result.append(d[i][0])
        return result

s = Solution()
print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))