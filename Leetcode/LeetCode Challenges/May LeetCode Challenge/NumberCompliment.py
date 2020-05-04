class Solution:
    def findComplement(self, num: int) -> int:
        # Approach 1:
        # Do the floor Division For the given number until the number is greater than 0
        # increment the count each time you do floor division
        # then return  pow(2,count)-1-given number
        # which will be the compliment of the given number
        if num == 0: return 1
        count = 0
        temp = num
        while num > 0:
            num = num // 2
            count += 1
        return 2 ** count - 1 - temp

        # Approach 1:
        # Convert the given number into its binary format
        # Replace all the 0's with 1's and 1's with 0's
        # convert this into decimal format

        bin_num = bin(num)[2:]
        res=""
        for i in bin_num :
            if i =='0':
                res += '1'
            else:
                res += '0'
        return int(res,2)
s = Solution()
print(s.findComplement(8))
