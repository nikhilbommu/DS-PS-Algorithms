def maxSubArray(nums) -> int:
    maxi = nums[0]
    sum1 = nums[0]
    for i in range(1, len(nums)):
        sum1 = max(sum1 + nums[i], nums[i])
        maxi = max(maxi, sum1)
    return maxi
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))