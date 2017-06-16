def solution(keys, values):
    '''Enter Code Here'''
    ans={}
    for i in range(0,len(keys)):
        ans[keys[i]]=values[i]
    return ans
