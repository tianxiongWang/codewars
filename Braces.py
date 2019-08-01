# C++不熟练，失败了，先用python实现
import queue

string = '[({})](]'

# 这个代码的思路就是创建一个lifo模型，然后查到返向括号就提取，用来判断是否
def validBraces(string):
    dic = {'(': ')', '[': ']', '{': '}'}
    List = queue.LifoQueue()
    for i in string:
        if i == '(' or i == '{' or i == '[':
            List.put(i)
        else:
            if i != dic[List.get()]:
                return False
            else:
                continue
    return True

if __name__ == "__main__":
    print(validBraces(string))