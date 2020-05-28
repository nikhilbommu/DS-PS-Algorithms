class Solution:
    def arrayPairSum(self, nums) -> int:
        nums = sorted(nums)
        sum1= 0
        for i in range(0,len(nums),2):
            sum1 += nums[i]
        return sum1

s = Solution()
print(s.arrayPairSum([1,4,3,2,5,6]))