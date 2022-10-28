from re import I
from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

def getDivisor(num) :
    divisorList = set()
    for i in range(2, num // 2 +1) :
        if num % i == 0 :
            divisorList.add(i)

    divisorList.add(num)
    return divisorList

result = []
xList = getDivisor(x) 

for i in a :
    if len(xList & getDivisor(i)) > 0 :
        continue
    else : result.append(i)

print(result)
print(sum(result) // len(result))