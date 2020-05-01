def singleNumber(nums):
    n = 0
    for i in nums:
        n = n ^ i
    return n
print(singleNumber([1,2,3,2,1]))