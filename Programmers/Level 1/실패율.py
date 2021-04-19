def solution(N, stages):
    answer = []
    lost = {}
    stages.sort()
    temp = []

    # N 수만큼 반복하면서
    for i in range(1, N+1):
        # 해당 스테이지가 배열에 포함되어 있으면
        num = 0
        for j in range(len(stages)): 
            if i == stages[j]:
                num += 1
        # stages 배열에서 i보다 같거나 큰 값의 개수
        users = len([x for x in stages if x >= i])
        lost[i] = num / users

    n = sorted(lost.items(), key=lambda x : x[1], reverse = True)
    return list(dict(n).keys())

print(solution(5, [2,1,2,6,2,4,3,3])) 