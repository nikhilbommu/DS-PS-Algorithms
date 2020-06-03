from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs) == 0:
            return 0
        pairs = sorted(pairs)
        result = [1]*len(pairs)
        for i in range(len(pairs)):
            for j in range(0,i):
                if pairs[i][0] > pairs[j][1]:
                    result[i] = max(result[i],result[j]+1)
        return max(result)

s = Solution()
print(s.findLongestChain([[1,2], [2,3], [3,4]]))
print(s.findLongestChain([[3,4],[2,3],[1,2]]))