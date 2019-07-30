
# >Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

# 其实就是把a到b之间的数求和，太简单了

def get_sum(a,b):
    if a == b:
        return a
    if a < b:
        sum = 0
        for num in range(a, b+1):
            sum += num
    else:
        sum = 0
        for num in range(b, a+1):
            sum += num
    return sum
