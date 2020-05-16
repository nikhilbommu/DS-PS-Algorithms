class Solution:
    def pivotIndex(self, nums) -> int:
        if len(nums) == 0:
            return -1
        Rsum = sum(nums)
        Lsum = 0
        for i in range(len(nums)):
            Lsum += nums[i]
            print(Lsum,Rsum)
            if Rsum == Lsum :
                return i
            Rsum -= nums[i]
        return -1

s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))