class Solution:
    def fourSumCount(A,B,C,D):
        res = 0
        dic = {}
        for i in A:
            for j in B:
                if i + j in dic:
                    dic[i + j] += 1
                else:
                    dic[i + j] = 1
        for i in C:
            for j in D:
                if 0 - (i + j) in dic:
                    res += dic[0 - (i + j)]
        return res
s=Solution
print(s.fourSumCount([1, 2],
[-2,-1],
[-1, 2],
[ 0, 2]))

