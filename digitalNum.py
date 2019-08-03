def digital(n):
    string = str(n)
    sum = 0
    for i in string:
        sum += int(i)
    if sum >= 10:
        return digital(sum)
    else:
        return sum


if __name__ == "__main__":
    print(digital(493193))