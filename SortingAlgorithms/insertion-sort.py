class Sorting:
    def insertion_sort(lis):
        for i in range(1,len(lis)):
            value=lis[i]
            hole=i
            while hole > 0 and lis[hole-1] > value:
                lis[hole] = lis[hole-1]
                hole-=1
            lis[hole]=value
        return lis

s=Sorting
print(s.insertion_sort([3,4,5,1,2,6]))