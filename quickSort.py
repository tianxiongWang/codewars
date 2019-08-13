import random
L1 = [random.randrange(0, 101) for i in range(100)]
print(L1)


def quickSort(L):
    if len(L) < 2:
        return L
    else:
        mid = L[0]
        L.remove(mid)
        less = [i for i in L if i <= mid]
        more = [i for i in L if i > mid]
        return quickSort(less) + [mid] + quickSort(more)


if __name__ == '__main__':
    print(quickSort(L1))
