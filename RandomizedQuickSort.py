import random

def RandomizedQuickSort(L):
    if (len(L) == 1) or (len(L) == 0):
        return L

    pivot = int(random.random() * len(L))
    left = []
    right = []

    for x in L[:pivot] + L[pivot+1:]:
        if (x < L[pivot]):
            left.append(x)
        else:
            right.append(x)
    return RandomizedQuickSort(left) + [L[pivot]] + RandomizedQuickSort(right)


A = list(range(20))
random.shuffle(A)

# 퀵정렬 전
print(A)

# 퀵정렬 후
print(RandomizedQuickSort(A))
