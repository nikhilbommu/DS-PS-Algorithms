from collections import Counter


class Solution:
    def intersect(nums1, nums2):
        intersection = []
        num1Dict = {}

        """for n in nums1:
            num1Dict[n] = num1Dict[n] + 1 if n in num1Dict else 1"""
        num1Dict = Counter(nums1)

        for n in nums2:
            if n in num1Dict and num1Dict[n] > 0:
                intersection.append(n)
                num1Dict[n] = num1Dict[n] - 1

        return intersection