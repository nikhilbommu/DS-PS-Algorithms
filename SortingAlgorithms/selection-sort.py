class Sorting:
    def selectionsort(arr):
        for i in range(len(arr)-1):
            iMin=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[iMin]:
                    iMin=j

            arr[i],arr[iMin]=arr[iMin],arr[i]
        return arr

s=Sorting
print(s.selectionsort([4,5,6,7,3,2,1]))