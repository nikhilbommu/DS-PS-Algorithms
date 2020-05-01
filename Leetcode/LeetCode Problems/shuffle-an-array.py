import random
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        nums_copy = self.nums[:]
        for i in range(n):
            j = random.randint(0, i)
            nums_copy[i], nums_copy[j] = nums_copy[j], nums_copy[i]
        return nums_copy
