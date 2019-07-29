# > Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

# >每个单词都有一个数字，再按照数字排序，我感觉可以用字典的特性

# 思路
# 1. python的sort方法很不错，应该可以完成这个问题，我以{num:word}的方式构建字典
# 毕竟，我听说python的字典现在是有序的了。接下来用sort排序
# 2. 关于提取num，我的想法是先按空格分开构成单个单词的数组，接下来利用ASCII码的特性。把数字拼接出来转化为数字类型，不然不好排序。
# 3. ord函数可转化asc码，chr函数转化字符串
# ord('0')=48
# rod('9')=57
# 4. 开始干活

def order(sentence):
    if sentence == '':
        return ''
    string_list = sentence.split(' ')
    result = []
    for word in string_list:
        num = ''
        for letter in word:
            if 48 <= ord(letter) <= 57:
                num += letter
        result.append((int(num), word))
    result.sort(key=lambda x: x[0], reverse=False)
    strings = []
    for i in result:
        strings.append(i[1])
    return ' '.join(strings)


if __name__ == "__main__":
    print(order(strings))