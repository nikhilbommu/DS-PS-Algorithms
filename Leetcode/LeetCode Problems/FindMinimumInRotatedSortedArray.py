class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        left,right = 0,len(nums)-1
        if nums[0] < nums[-1]:
            return nums[0]
        while left<=right:
            mid = left + (right - left) //2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

s = Solution()
print(s.findMin([3,4,5,6,1,2]))