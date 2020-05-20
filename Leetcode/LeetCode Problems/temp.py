def largest():
    res = []
    lst = [10,20,30]
    for i in range(len(lst)):
        lst[i] = str(lst[i])
        c = 0
        for j in range(len(lst[i])):
            if int(lst[i][j]) == lst[i].count(j):
                c += 1
        if c == len(lst[i]):
            res.append(lst[i])
    print(len(res))

largest()
