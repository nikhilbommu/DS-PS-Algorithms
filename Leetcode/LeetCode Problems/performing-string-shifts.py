class Solution:
    def stringShift(s,shift):
        count = 0
        for i in shift:
            if i[0] == 0:
                count -= i[1]
            else:
                count += i[1]
        count = count % len(s)
        if count == 0:
            return s
        if count < 0:
            temp = s[:count]
            s = s.replace(temp, '')
            s += temp
            return s
        if count > 0:
            temp = s[len(s) - count:]
            s = s.replace(temp, '')
            temp += s
            return temp


s = Solution
print(s.stringShift("wpdhhcj", [[0, 7], [1, 7], [1, 0], [1, 3], [0, 3], [0, 6], [1, 2]]))