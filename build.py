def solution(keys, values):
    for x, y in zip(keys,values):
        dic[x] = y
    return dic

dic = {}
lis1 = []
lis2 = []
solution(lis1, lis2)
