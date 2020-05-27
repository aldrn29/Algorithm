import random

def Merge(A, B):
    if (len(A) == 0):
        return B
    if (len(B) == 0):
        return A
    if (A[0] < B[0]):
        return [A[0]] + Merge(A[1:], B)
    else:
        return [B[0]] + Merge(A, B[1:])

def MergeSort(L):
    if (len(L) == 1):
        return L
    return Merge(MergeSort(L[:int(len(L)/2)]), MergeSort(L[int(len(L)/2):]))

A = list(range(10))
random.shuffle(A)

# 병합정렬 전
print(A)

# 병합정렬 후
print(MergeSort(A))
            
