def solution(l1,l2):
    k = zip(l1,l2)
    d = dict()
    for (x,y) in k:

        if x in d:
            d[x] = d[x] + y
        else:
            d[x] = y

    return d
print solution([1,2,3],[10,20,30])
