###
# permutations
###

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

str_max = str(max_num)
str_min = str(min_num)

if len(str_max) != k+1 : str_max = '0' + str_max
if len(str_min) != k+1 : str_min = '0' + str_min

print(str_max)
print(str_min)


###
# backtracking 
###

from sys import stdin

k = int(input())
s_list = list(map(str, stdin.readline().split())) 

visited = [0]*10
max_num = ""
min_num = ""

def check(i, j, sign) :
    if sign =='<' :
        return i<j
    else: return i>j

def solve(idx, s) :
    global max_num,min_num

    if idx == k+1 :
        if len(min_num) == 0 :
            min_num = s
        else : max_num = s
        return

    for i in range(10) : 
        if visited[i] == 0 :
            if idx == 0 or check(s[-1], str(i), s_list[idx]) :
                visited[i] = True
                solve(idx+1, s+str(i))
                visited[i] = False

solve(-1, "")
print(max_num)
print(min_num)