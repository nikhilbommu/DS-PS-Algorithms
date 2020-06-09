from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst = []
        temp = n
        i = 0
        while i < temp:
            lst.append(nums[i])
            lst.append(nums[n])
            i, n = i + 1, n + 1

        return lst

s = Solution()
print(s.shuffle([2,5,1,3,4,7],3))
