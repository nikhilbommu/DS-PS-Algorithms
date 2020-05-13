class Solution:
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"
        i = 0
        num = list(num)
        while k > 0:
            i = i - 1 if i > 0 else 0
            while i < len(num) - 1 and num[i] <= num[i + 1]:
                i += 1
            del num[i]
            k -= 1

        i = 0
        while i < len(num) and num[i] == '0':
            i += 1
        if i > 0:
            num = num[i:]
        if len(num) == k:
            return "0"
        return ''.join(num)

s = Solution()
print(s.removeKdigits("87654",3))