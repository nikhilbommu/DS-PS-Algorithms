class Sorting:
    def bubblesort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

s=Sorting
print(s.bubblesort([4,5,6,7,3,2,1]))