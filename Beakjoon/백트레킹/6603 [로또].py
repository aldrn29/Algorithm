###
# combinations
###

from sys import stdin
from itertools import combinations

while True :
    s = list(map(int, stdin.readline().split()))
    k = s.pop(0)

    if k == 0 :
        break

    comb = combinations(s, 6)
    for i in comb :
        print(' '.join(map(str, i)))
    print()