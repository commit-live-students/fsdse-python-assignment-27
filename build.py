# Map two lists into a dictionary

a = [1, 2, 3]
b = [10, 20, 30]

def solution(a,b):
    dic = {}
    for i in range(len(a)):
        dic[a[i]] = b[i]
    return dic

solution(a,b)

#DOne, Not Posted =================================================================================
