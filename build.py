import itertools

def solution(keys, values):
    newdict = dict(itertools.izip(keys,values))
    return newdict


print solution([1, 2, 3], [10, 20, 30])
