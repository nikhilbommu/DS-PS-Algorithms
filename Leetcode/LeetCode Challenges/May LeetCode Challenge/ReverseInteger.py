class Solution:
    def reverse(self, x) -> int:
        temp = x
        x = abs(x)
        mul = 10 ** (len(str(x)) - 1)
        res = 0

        while x > 0:
            rem = x % 10
            res = res + rem * mul
            mul = mul // 10
            x = x // 10
        if res > pow(2, 31):
            return 0
        if temp > 0:
            return res
        return -res


s = Solution()
print(s.reverse(12345))