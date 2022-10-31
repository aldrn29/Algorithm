# from sys import stdin
# input = stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# x = int(input())

# def getDivisor(num) :
#     divisorList = set()
#     for i in range(2, num // 2 +1) :
#         if num % i == 0 :
#             divisorList.add(i)

#     divisorList.add(num)
#     return divisorList

# result = []
# xList = getDivisor(x) 

# for i in a :
#     if len(xList & getDivisor(i)) > 0 :
#         continue
#     else : result.append(i)

# print(sum(result) // len(result))

n = int(input())
a = list(map(int, input().split()))
x = int(input())
result = 0
cnt = 0

def getDivisor(num) :
    divisorList = []
    for i in range(1, int(num**0.5)+1) :
        if num % i == 0 :
            divisorList.extend([i, num//i])
    divisorList.remove(1)
    return list(set(divisorList))

xList = getDivisor(x)

for num in a :
    for x in xList : # 4의 약수 [2 ,4]
        if num % x == 0 : # [4,2,8,5,7] 이 4의 약수(2)로 나뉘면
            break
    else :
        result += num
        cnt += 1

print(result / cnt)