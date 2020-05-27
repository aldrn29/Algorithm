import random

def InsertSort(L):
    temp = list(L)
    result = []

    while (len(temp) > 0):
        m = temp.pop(0)
        result.append(m)
        
        for i in range(1, len(result))[::-1]:
            if(result[i] < result[i-1]):
                result[i], result[i-1] = result[i-1], result[i]
            else:
                break
    return result

A = list(range(20))
random.shuffle(A)

# 삽입정렬 전
print(A)

# 삽입정렬 후
print(InsertSort(A))
