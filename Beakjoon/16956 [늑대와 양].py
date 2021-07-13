row, col = map(int, input().split())
m = [input() for _ in range(row)]

def function() :
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x = 0
    y = 0

    for i in range(row) :
        for j in range(col) : 
            if m[i][j] != 'W' : continue

            for d in range(4) :
                if (d == 0 and i <= 0) or (d == 1 and j >= col-1) or (d == 2 and i >= row-1) or (d == 3 and j <= 0) : continue
                x = i + dx[d]
                y = j + dy[d]
                #print('d=', d, 'dx=', dx[d], 'dy=', dy[d], 'x=', x, 'y=', y)
                if m[x][y] != '.' and m[x][y] != 'W': 
                    return 0
    return 1

value = function()
if value == 1 :
    print(value) 
    for i in range(row) :
        s = m[i].replace('.', 'D')
        print(s)
else :
    print(value)
