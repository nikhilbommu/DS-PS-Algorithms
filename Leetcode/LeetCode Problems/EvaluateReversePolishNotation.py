class Solution:
    def evalRPN(self, tokens) -> int:
        lst = []
        i = 0
        while i < len(tokens):
            if tokens[i] not in "+-*/":
                lst.append(int(tokens[i]))
            else:
                t1 = lst.pop()
                t2 = lst.pop()

                if tokens[i] == '+':
                    lst.append(t2 + t1)
                elif tokens[i] == '-':
                    lst.append(t2 - t1)
                elif tokens[i] == '*':
                    lst.append(t2 * t1)
                elif tokens[i] == '/':
                    lst.append(int(t2 / t1))
            i += 1
        return lst[0]

s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
