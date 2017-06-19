def solution(keys, values):
    dict1 = {}
    for i in range(len(keys)):
        dict1[keys[i]] = values[i]

    return dict1

keys = [1, 2, 3, 4]
values = [5, 6, 7, 8]
solution(keys, values)
