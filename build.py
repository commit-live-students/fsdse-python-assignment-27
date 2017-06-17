def solution(keys, values):
    ls = []
    ls = zip(keys,values)
    ls=dict(ls)
    print ls
    return ls

solution([1,2,3,4],['a','b','c','d'])
