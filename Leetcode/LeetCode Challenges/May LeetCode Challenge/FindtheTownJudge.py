class Solution:
    def findJudge(self, N, trust) -> int:
        dct = {}
        for i in range(1, N + 1):
            dct[i] = 0
        people = [trust[i][0] for i in range(len(trust))]

        for i in range(len(trust)):
            dct[trust[i][1]] += 1

        for val in dct:
            if dct[val] == N - 1 and val not in people:
                return val
        return -1

s = Solution()
print(s.findJudge(3,[[1,3],[2,3]]))