def titleToNumber(s: str):
    sum1 = 0
    if len(s) == 0:
        return -1
    for i in range(len(s)):
        sum1 *= 26
        sum1 += ord(s[i]) - ord('A') + 1
    return sum1

print(titleToNumber('AB'))