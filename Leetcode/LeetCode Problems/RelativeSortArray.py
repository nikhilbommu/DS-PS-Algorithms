from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            total = arr1.count(i)
            result += [i] * total

        rem_lst = []
        for i in arr1:
            if i not in arr2:
                rem_lst.append(i)
        rem_lst = sorted(rem_lst)
        return result + rem_lst

s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))