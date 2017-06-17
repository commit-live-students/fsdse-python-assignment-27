def solution(keys, values):
     return {k: v for k,v in zip(keys,values)}

print solution([1, 2, 3], [10, 20, 30])
