from sys import stdin

num = int(stdin.readline()) # 7
graph = [list(map(int, stdin.readline().split())) for _ in range(num)]

# dfs
def dfs(v):
    for i in range(num): # 7
        if check[i] == 0 and graph[v][i] == 1:
            check[i] = 1
            dfs(i)

for x in range(num): # 7
    check = [0 for _ in range(num)]
    dfs(x)
    print(*check)
