import random

def BubbleSort(L):
    result = list(L)
    
    for x in range(len(result)-1):
        for y in range(len(result)-x-1):
            if (result[y] > result[y+1]):
                result[y], result[y+1] = result[y+1], result[y]
    return result

A = list(range(20))
random.shuffle(A)

# 버블정렬 전
print(A)

# 버블정렬 후
print(BubbleSort(A))
