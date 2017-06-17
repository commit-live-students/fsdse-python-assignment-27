def solution(keys, values):
    '''Enter Code Here'''
    new_dic = {}
    for i,v in enumerate(values):
        i +=1
        d = dict({i : v})
        new_dic.update(d)
    return new_dic



keys = [1, 2, 3]
vals = [10, 20, 30]
print(solution(keys, vals))
