###
# combinations
###

from itertools import combinations

n, m = list(map(int,input().split()))
l = list(map(int, input().split()))
l.sort()

pmt = list(combinations(l, m))
result = sorted(list(set(pmt))) # 중복 제거 후 오름차순 정렬

for i in pmt :
    for j in range(m) :
        print(i[j], end=' ')
    print()
