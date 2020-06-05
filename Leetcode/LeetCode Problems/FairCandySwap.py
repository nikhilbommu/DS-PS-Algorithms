from typing import List
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B)-sum(A))//2
        setA = set(A)
        setB = set(B)
        for each in setA:
            if each + diff in setB:
                return [each, each + diff]

s = Solution()
print(s.fairCandySwap([1,1],[2,2]))