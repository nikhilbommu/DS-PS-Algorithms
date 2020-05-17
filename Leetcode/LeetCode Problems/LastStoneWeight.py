class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) != 1:
            maxi1 = max(stones)
            stones.remove(maxi1)
            print(stones)
            maxi2 = max(stones)
            stones.remove(maxi2)
            print(stones)
            stones.append(abs(maxi1-maxi2))
        return stones
s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))