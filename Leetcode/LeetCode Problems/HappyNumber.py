def isHappy( n: int) -> bool:
    set1 = set()
    while n not in set1 and n != 1:
        sum1=0
        set1.add(n)
        for i in str(n):
            sum1+=int(i) ** 2
        n=sum1
    return n == 1


print(isHappy(29))  # Expected Output : False
