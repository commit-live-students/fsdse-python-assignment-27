def solution(keys, values):
    d={}

    for i in range(0,len(keys)):
        d[keys[i]]=values[i]
    return d

print(solution([1, 2, 3], [10, 20, 30])) 
