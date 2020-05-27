import random

def QuickSort(L):
    if (len(L) == 1) or (len(L) == 0):
        return L

    pivot = L[0]
    left = []
    right = []

    for x in L[1:]:
        if (x < pivot):
            left.append(x)
        else:
            right.append(x)
    return QuickSort(left) + [pivot] + QuickSort(right)


A = list(range(20))
random.shuffle(A)

# 퀵정렬 전
print(A)

# 퀵정렬 후
print(QuickSort(A))
