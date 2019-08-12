def increment_string(string):
    key = -1
    num = ''
    for i in range(len(string) - 1, -1, -1):
        if ord(string[i]) < 48 or ord(string[i]) > 57:
            key = i
            break
        num += string[i]
    if key == len(string) - 1:
        return string + '1'       
    if key != -1:
        finallyNum = num[-1::-1]
        length = len(finallyNum)
        resultNum = str(int(finallyNum) + 1).zfill(length)
        result = string[0:key+1] + resultNum
        return result
    else:
        length = len(string)
        result = str(int(string) + 1).zfill(length)
        return result


print(increment_string('foo'))