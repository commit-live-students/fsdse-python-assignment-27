def solution(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary.update({keys[i]:values[i]})
    return dictionary
