from itertools import combinations

expression = input().strip()
pair = []
temp = []
result = set()

# ()의 쌍을 찾는다. [(3, 5), (0, 6)]
for index, word in enumerate(expression) :
    if word == '(' :
        temp.append(index)
    elif word == ')' :
        pair.append((temp.pop(), index))

# 모든 경우의 수를 구한다.
for i in range(1, len(pair)+1) :
    cases = combinations(pair, i)

    for j in cases :
        ex = list(expression)
        for (start, end) in j :
            ex[start] = ""
            ex[end] = ""

        result.add(''.join(ex))

for r in sorted(list(result)):
    print(r)