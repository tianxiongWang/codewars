def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr or k <= 0):
        return ""
    num = [len(i) for i in strarr]
    const = len(strarr) - k + 1
    value = []
    for i in range(const):
        sum = 0
        for j in range(k):
            sum += num[i + j]
        value.append(sum)
    index = value.index(max(value))
    result = ''
    for i in range(index, index + k):
        result += strarr[i]
    return result
if __name__ == "__main__":
    strarr = ["zone", "abigail", "theta", "form", "libe", "zas"]
    print(longest_consec(strarr, 2))