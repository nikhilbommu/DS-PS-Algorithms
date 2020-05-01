class Solution:
    def generate(openCount, closeCount, tempStr, lis):
        if openCount < 0 or closeCount < 0:
            return
        elif openCount == 0 and closeCount == 0:
            lis.append(tempStr)
        elif openCount < closeCount:
            s.generate(openCount - 1, closeCount, tempStr + "(", lis)
            s.generate(openCount, closeCount - 1, tempStr + ")", lis)
        elif openCount == closeCount:
            s.generate(openCount - 1, closeCount, tempStr + "(", lis)

    def generateParenthesis(n):
        openCount, closeCount = n, n
        lis = []
        s.generate(openCount, closeCount, "", lis)
        return lis
s=Solution
print(s.generateParenthesis(4))