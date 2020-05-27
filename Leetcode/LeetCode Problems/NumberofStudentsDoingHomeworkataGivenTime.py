class Solution:
    def busyStudent(self, startTime, endTime, queryTime) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count

s = Solution()
print(s.busyStudent([9,8,7,6,5,4,3,2,1],[10,10,10,10,10,10,10,10,10],5))