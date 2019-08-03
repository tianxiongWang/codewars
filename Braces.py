# C++不熟练，失败了，先用python实现
import queue
import time
string = "[({})](][](()){}{}{}{}}{"

# 这个代码的思路就是创建一个lifo模型，然后查到返向括号就提取，用来判断是否正确闭合
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

# 使用另一套思路，用x， z， d代表三个括号，每一次循环这三个数都必须为正数，小于0就说明未闭合，来做一下
def validBraces2(string):
    x, z, d = 0, 0, 0
    for i in string:
        if i == '(':
            x += 1
        if i == '[':
            z += 1
        if i == '{':
            d += 1
        if i == ')':
            x -= 1
        if i == ']':
            z -= 1
        if i == '}':
            d -= 1
        if x < 0 or z < 0 or d < 0:
            return False
            break
    if x == 0 and z == 0 and d == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    begin1 = time.time()
    print(validBraces(string))
    over1 = time.time()
    print((over1 - begin1) * 10 ** 9)
    begin2 = time.time()
    print(validBraces2(string))
    over2 = time.time()
    print((over2 - begin2) * 10 ** 9)
    #方法二效率得到显著提高