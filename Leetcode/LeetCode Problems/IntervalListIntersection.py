class Solution:
    def intervalIntersection(self, A, B) :
        result = []
        Astart, Bstart = 0, 0
        while Astart < len(A) and Bstart < len(B):
            low = max(A[Astart][0], B[Bstart][0])
            high = min(A[Astart][1], B[Bstart][1])
            if low <= high:
                result.append([low, high])

            if A[Astart][1] < B[Bstart][1]:
                Astart += 1
            else:
                Bstart += 1

        return result

s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))