class Solution:
    def constructRectangle(self, area: int):
        result = []
        for i in range(2, area + 1):
            if area % i == 0:
                temp = area // i
                result.append([i, temp])
        mini_list = []
        for i in result:
            mini_list.append(abs(i[0] - i[1]))
        if len(mini_list) != 0:
            mini = min(mini_list)
        else:
            return [1, 1]
        ind = mini_list.index(mini)
        return sorted(result[ind], reverse=True)

s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(100))