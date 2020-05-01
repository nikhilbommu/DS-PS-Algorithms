class mergesort:
    def merge_sort(arr):
        n = len(arr)
        if n<2:
            return
        mid=n//2
        left=arr[:mid]
        right=arr[mid:]
        s.merge_sort(left)
        s.merge_sort(right)
        i,j,k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        return arr
s=mergesort
arr=[10,9]
print(s.merge_sort(arr))