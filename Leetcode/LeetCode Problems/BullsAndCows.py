class Solution:
    def getHint(self, secret, guess):
        bc, cc = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bc += 1
        for i in set(secret):
            cc += min(secret.count(i), guess.count(i))
        return str(bc) + "A" + str(cc - bc) + "B"

s = Solution()
print(s.getHint("1807","7810"))