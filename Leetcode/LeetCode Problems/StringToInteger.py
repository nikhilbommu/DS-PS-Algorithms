class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0:
            return 0
        result_str = "0"
        result = 0
        i = 0
        if str[0] in "+-":
            result_str = str[0]
            i = 1
        for i in range(i, len(str)):
            if str[i].isdigit():
                result_str += str[i]
            else:
                break
        if len(result_str) > 1:
            result = int(result_str)
        if result >= 2 **31 :
            return 2**31-1
        elif result < -2 ** 31:
            return -2 ** 31
        else:
            return result

s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("4193 with words"))