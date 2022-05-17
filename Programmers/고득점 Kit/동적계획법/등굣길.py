def solution(m, n, puddles):
    matrix = [[0] * (m+1) for _ in range(n+1)]
    matrix[1][1] = 1

    for x in range(1, n+1) :
        for y in range(1, m+1) :
            if x == 1 and y == 1 : continue
            
            if [y, x] in puddles :
                 matrix[x][y] = 0
            else :
                matrix[x][y] = matrix[x-1][y] + matrix[x][y-1]

    return matrix[n][m] % 1000000007


print(solution(4, 3, [[2,2]]))