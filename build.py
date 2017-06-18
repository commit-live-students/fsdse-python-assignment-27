def solution(ls1, ls2):
    dic = {}
    for x in range(len(ls1)):
        dic.update({ls1[x]:ls2[x]})
    return dic
