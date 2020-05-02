class Solution:
    def numJewelsInStones(self, J, S) -> int:
        """
        Approach:1 using dictionary
        storing the (key,value) pairs of Jewels in dictionary
        Iterating through the stones and updating the value of count
        """
        dct = {}
        count = 0
        for i in J :
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
        for j in S :
            if j in dct.keys():
                count+=dct[j]
        print(count)

        #Approach 2:
        #Iterating through Stones and checking if it is in Jewels
        #If exists then incrementing the count
        count1 = 0
        for i in S:
            if i in J:
                count1 += 1
        print(count1)

s = Solution()
s.numJewelsInStones("aA","aAAbcc")