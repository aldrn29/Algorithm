###
# permutations
###

from sys import stdin
from itertools import permutations

n = int(input())
l = list(map(int, stdin.readline().split()))

comb_list = permutations(l, n)
l_max = 0

for comb in comb_list :
    t_sum = 0
    for i in range(n-1) :
        t_sum += abs(comb[i] - comb[i+1])
    
    l_max = max(l_max, t_sum)

print(l_max)