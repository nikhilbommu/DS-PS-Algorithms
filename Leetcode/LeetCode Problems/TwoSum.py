class Solution:
    def twoSum(self, numbers, target):
        dct = {}
        for index,value in enumerate(numbers):
            if value in dct:
                return [dct[value],index]
            dct[target -value] = index

s = Solution()
print(s.twoSum([2,3,3,15],6))