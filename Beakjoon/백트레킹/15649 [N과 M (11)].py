from sys import stdin

n, m = map(int, stdin.readline().split())
l = list(sorted(set(map(int, stdin.readline().split()))))
result = []

def dfs() :
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for i in l :
        result.append(i)
        dfs()
        result.pop()

dfs()