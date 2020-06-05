class Solution:
    def reformat(self, s: str) -> str:
        words, nums = [], []
        for i in s:
            if i.isalpha():
                words.append(i)
            else:
                nums.append(i)
        result = ""
        if (len(words) == 0 and len(nums) > 1) or (len(nums) == 0 and len(words) > 1):
            return ""
        if len(words) > len(nums):
            ws, ns = 0, 0
            while ws < len(words) and ns < len(nums):
                result += words[ws]
                result += nums[ns]
                ws += 1
                ns += 1
            while ws < len(words):
                result += words[ws]
                ws += 1
        else:
            ws, ns = 0, 0
            while ws < len(words) and ns < len(nums):
                result += nums[ns]
                result += words[ws]
                ws += 1
                ns += 1
            while ns < len(nums):
                result += nums[ns]
                ns += 1

        return result

s = Solution()
print(s.reformat("a0b1c2"))