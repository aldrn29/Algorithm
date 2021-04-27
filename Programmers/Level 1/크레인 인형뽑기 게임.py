def solution(board, moves):
    answer = 0
    temp = []
    N = len(board)

    for i in moves:
        for j in range(N):
            if board[j][i-1] != 0:
                temp.append(board[j][i-1])
                board[j][i-1] = 0
                break
        
        if len(temp) > 1 and temp[-1] == temp[-2]:
            temp.pop()
            temp.pop()
            answer += 2

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))