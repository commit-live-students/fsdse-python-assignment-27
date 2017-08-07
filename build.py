def solution(keys, values):
    output = {}
    for k, v in zip (keys, values):
        output[k] = v

    return output
