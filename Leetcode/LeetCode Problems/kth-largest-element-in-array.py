from heapq import heappush, heappop
class Solution:
    def findKthLargest(nums,k) -> int:
        num1 = []
        res = -1
        for i in nums:
            heappush(num1, i)
        k = len(nums) - k + 1
        for i in range(k):
            res = heappop(num1)
        return res
s=Solution
print(s.findKthLargest([1,2,3,4,5,6,7,8],2))
