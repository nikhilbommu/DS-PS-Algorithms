class Solution:
    #using binary search
    def findPeakElement(nums):
        low,high = 0,len(nums)-1
        while(low<high):
            mid = low+(high-low)//2
            if nums[mid]<nums[mid+1]:
                low = mid+1
            else:
                high = mid
        return low
    """
    #normal for loop method
        if len(nums)<=1:
            return 0
        nums.append(nums[0])
        for i in range(len(nums)):
            if nums[i]>nums[i+1]:
                return i
        return 1
       """
    print(findPeakElement([1,2,3]))