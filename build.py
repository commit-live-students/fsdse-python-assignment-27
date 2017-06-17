def solution(keys, values):
    '''Enter Code Here'''
    dict = {}
    i = len(keys)
    for i in range(0,i):
        dict[keys[i]]=values[i]
    return dict
