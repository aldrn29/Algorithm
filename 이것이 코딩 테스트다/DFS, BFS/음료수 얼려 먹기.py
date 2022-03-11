n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

visited = [[False] * m for _ in range(n)]

def dfs(x, y) :
    if (0 <= x < n and 0 <= y < m) :
        if visited[x][y] : return False
        visited[x][y] = True

        if graph[x][y] == 0 :
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
        
        return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result += 1

print(result)

# 입력 예시
'''
4 5
00110
00011
11111
00000
'''