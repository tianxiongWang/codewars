def pick_peaks(arr):
    dic = dict()
    dic['pos'] = list()
    dic['peaks'] = list()
    key = 0
    count = 0
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1]:
            key += 1
        if arr[i] > arr[i+1]:
            key += 1
        if arr[i] == arr[i+1]:
            count += 1
            continue
        if key == 2:
            dic['pos'].append(i-count)
            dic['peaks'].append(arr[i])
        key = 0
        count = 0
    print(dic)
    return dic


pick_peaks([4, 4, 4, 3])
