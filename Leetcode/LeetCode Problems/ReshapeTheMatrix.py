import numpy as np
class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        if len(nums) * len(nums[0]) == r * c:
            return np.reshape(nums, (r, c))
        return nums

s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))