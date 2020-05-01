#DP solution for climbing 1step or 2steps at a time
class Solution:
    def climbStairs(n: int) :
        l = [1, 1]
        for i in range(2, n + 1):
            l.append(l[i - 1] + l[i - 2])
        return l[n]
    print(climbStairs(6))

