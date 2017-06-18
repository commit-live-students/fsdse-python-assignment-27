def solution(x,y):
    dic = {}
    if len(x) == len(y):
        z = 0
        for i in x:
            dic[i] = y[z]
            z = z+1
    return dic
solution([1, 2, 3], [10, 20, 30])
