class Solution:
    def maximum69Number(self, num: int) -> int:
        temp = num
        add = 0
        mul = 1
        while num > 0:
            rem = num % 10
            if rem == 6:
                add = 3 * mul
            mul = mul * 10
            num = num // 10
        return temp + add
s = Solution()
print(s.maximum69Number(9699))