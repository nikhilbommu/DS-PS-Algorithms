class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        total_sum = 0
        curr_min = 0
        curr_max = 0
        max_sum = -999999
        min_sum = 999999
        for i in A:
            total_sum += i
            curr_max = max(curr_max + i, i)
            max_sum = max(curr_max, max_sum)
            curr_min = min(curr_min + i, i)
            min_sum = min(curr_min, min_sum)

        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        return max_sum

s = Solution()
print(s.maxSubarraySumCircular([1,-2,3,-2]))