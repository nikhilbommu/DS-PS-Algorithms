from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedarray = sorted(set(arr))
        dct = {}
        result = []
        for i,j in enumerate(sortedarray,start=1):
            dct[j] = i
        for i in arr:
            result.append(dct[i])
        return result

s = Solution()
print(s.arrayRankTransform([40,10,20,30]))