def solution(keys, values):
    '''Enter Code Here'''
    d = {}
    x = 0
    for i in keys:
        d[i] = values[x]
        x = x + 1
    return d
