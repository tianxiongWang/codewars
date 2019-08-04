def alphabet_position(text):
    dic = dict()
    for k, num in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)):
        dic[k] = num
    for k, num in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)):
        dic[k] = num
    result_list = list()
    for alphabet in text:
        if 65 <= ord(alphabet) <= 90 or 97 <= ord(alphabet) <= 122:
            result_list.append(str(dic[alphabet]))
    result = ' '.join(result_list)
    return result

if __name__ == "__main__":
    print(alphabet_position("The sunset sets at twelve o' clock."))