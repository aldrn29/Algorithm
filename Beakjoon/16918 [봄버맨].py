from sys import stdin

row, col, n = map(int, stdin.readline().split())
bomb = [[0]*col for _ in range(row)]

for i in range(row) :
    m = list(stdin.readline().strip())
    for j in range(col) :
        if m[j] == 'O' : bomb[i][j] = 1

def explosion() :
    sec = 0

    while True :
        if sec >= n :
            for i in range(row) :
                for j in range(col) :
                    if bomb[i][j] > 0 : print('O', end='')
                    else : print('.', end='')
                print()
            return

        sec += 1
        for i in range(row) :
            for j in range(col) :
                if bomb[i][j] > 0 : bomb[i][j] += 1

        # 비어있는 칸에 폭탄 채우기
        if sec % 2 == 0 :
            for i in range(row) :
                for j in range(col) :
                    if bomb[i][j] == 0 : bomb[i][j] = 1
        else : # 3초가 된 폭탄 터트리기
            if sec == 1 : continue 
            b = []
            for i in range(row) :
                for j in range(col) :
                    if bomb[i][j] > 3 : # 폭탄 터짐
                        b.append((i, j))
                        bomb[i][j] = 0
            for i in range(len(b)) : # 폭탄 주변 터트리기
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
                    nx = b[i][0] + dx
                    ny = b[i][1] + dy
                    if 0 <= nx < row and 0 <= ny < col :
                        bomb[nx][ny] = 0

explosion()