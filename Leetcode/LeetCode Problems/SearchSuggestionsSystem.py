class Solution:
    def suggestedProducts(self, products , searchWord: str) :
        matrix = []
        search = ""
        products = sorted(products)
        for i in searchWord:
            search += i
            count = 0
            temp = []
            for j in products:
                if j.startswith(search):
                    count += 1
                    temp.append(j)

            if count > 2:
                matrix.append(temp[:3])
            else:
                matrix.append(temp)
        return matrix

s = Solution()
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))