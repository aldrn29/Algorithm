from sys import stdin
from itertools import permutations

k = int(input())
s = list(map(str, stdin.readline().split())) 

num = permutations(range(10), k+1) 
min_num = 9999999999
max_num = 0

for i in num :
    for j in range(k) :
        if (s[j] == '<' and i[j] < i[j+1]) or (s[j] == '>' and i[j] > i[j+1]) : 
            if j == k-1 :
                max_num = max(max_num, int(''.join(map(str, i))))
                min_num = min(min_num, int(''.join(map(str, i))))
            continue
        else : break

# 앞에 0 추가하기
print(max_num)
print(min_num)