from sys import stdin

n, m = map(int, stdin.readline().split())
l = list(sorted(set(map(int, stdin.readline().split()))))
result = []

def dfs(start) :
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for i in range(start, len(l)) :
        result.append(l[i])
        dfs(i)
        result.pop()

dfs(0)