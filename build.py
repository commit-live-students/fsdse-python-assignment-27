def solution(keys, values):
    '''Enter Code Here'''
    assert len(keys) == len(values), ' both the lists shold have equal length'
    k = list(keys)
    v = list(values)
    d = {}
    for k, v in list(zip(keys, values)):
        d[k] = v
    return d
