import sys
class Solution:
    def maxProfit(prices) -> int:
        maxprice = 0
        minprice = sys.maxsize
        for i in range(len(prices)):
            minprice = min(minprice,prices[i])
            maxprice = max(maxprice,prices[i]-minprice)
        return maxprice


    print(maxProfit([7,1,5,3,6,4]))