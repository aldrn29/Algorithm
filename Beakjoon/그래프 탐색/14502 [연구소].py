from sys import stdin
from collections import deque
from itertools import combinations
from copy import deepcopy

def bfs(matrix) :
    queue = deque()
    visited = [[False]*col for _ in range(row)]
    cnt = 0

    # 바이러스 확산
    for x, y in virus :
        queue.append((x,y))

        while queue :
            x, y = queue.popleft()

            if visited[x][y] : continue
            else : visited[x][y] = True

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < row and 0 <= ny < col :
                    if matrix[nx][ny] == 0 and visited[nx][ny] == False :
                        matrix[nx][ny] = 2
                        queue.append((nx, ny))

    # 안전영역 카운트
    for i in range(row) :
        for j in range(col) :
            if matrix[i][j] == 0 :
                cnt += 1

    return cnt


def solve() :
    # 안전영역에서 벽 3개를 세울 수 있는 조합 모두 뽑음
    wall_list = list(combinations(safe, 3))
    count = 0
    
    for w in wall_list :
        tm = deepcopy(m)
        tm[w[0][0]][w[0][1]], tm[w[1][0]][w[1][1]], tm[w[2][0]][w[2][1]] = 1, 1, 1

        # 벽이 세워진 채로 탐색하여 안전공간 리턴 
        cnt = bfs(tm)
        count = max(count, cnt)
    
    return count


row, col = map(int, input().split()) 
m = [list(map(int, stdin.readline().split())) for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

safe = []
virus = []

for i in range(row) : # 0 빈칸, 1 벽, 2 바이러스
    for j in range(col) :
        if m[i][j] == 1 : continue
        if m[i][j] == 0 : safe.append((i, j))
        else : virus.append((i, j))

print(solve())
