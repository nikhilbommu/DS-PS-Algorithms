class Solution:
    def isPalindrome(self, x) -> bool:
        temp = x
        if x<0:
            return False
        res = 0
        mul = 1
        while x > 0:
            rem = x % 10
            res += rem * mul
            mul = mul*10
            x = x//10
        if str(temp) == str(res)[::-1]:
            return True
        return False

s = Solution()
print(s.isPalindrome(121))