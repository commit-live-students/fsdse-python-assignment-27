def solution(keys, values):
    dictionary = dict()
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary

a = [1, 2, 3]
b = [10, 20, 30]
print solution(a,b)
