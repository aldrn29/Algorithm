def solution(answers):
    result = [0, 0, 0]
    player1 = [1, 2, 3, 4, 5]
    player2 = [2, 1, 2, 3, 2, 4, 2, 5]
    player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)) :
        if answers[i] == player1[i % 5]:
            result[0] += 1
        if answers[i] == player2[i % 8]:
            result[1] += 1
        if answers[i] == player3[i % 10]:
            result[2] += 1

    max_answer = max(result)
    answer = []
    for i in range(3) :
        if max_answer == result[i] :
            answer.append(i+1)
    
    return answer
            