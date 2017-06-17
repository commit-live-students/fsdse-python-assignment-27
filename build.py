def solution(keys, values):
    '''TO get the key value pair thru two different list as form of dictionary'''
    new_dic = {k: v for k,v in zip(keys,values)}
    print new_dic
    return new_dic

solution([1, 2, 3], [10, 20, 30])
