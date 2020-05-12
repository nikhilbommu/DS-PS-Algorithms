class Solution:
    def singleNonDuplicate(self, nums) -> int:
        #Approach 1: Using Counter
        """c = Counter(nums)
        for i in c:
            if c[i] == 1:
                return i
        return -1"""
        #Approach 2 : using sets
        """return sum(set(nums))*2 - sum(nums)"""


        #Approach 3: using XOR operation
        """temp = 0
        for i in nums:
            temp ^= i

        return temp"""
        #Approach 4 : Binary Search
        ln = len(nums)
        if ln == 1:
            return nums[0]

        start, end = 0, ln - 1
        while start <= end:
            mid = (end - start) // 2 + start
            if (mid == 0 or nums[mid - 1] != nums[mid]) and (mid == ln - 1 or nums[mid + 1] != nums[mid]):
                return nums[mid]

            if (mid == 0 or nums[mid - 1] == nums[mid]) and (mid + 1) % 2 == 0:
                start = mid + 1
            elif (mid == ln - 1 or nums[mid + 1] == nums[mid]) and (mid) % 2 == 0:
                start = mid + 2
            else:
                end = mid - 1

s = Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4]))

