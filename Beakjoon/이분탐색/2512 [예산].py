from sys import stdin

num = int(stdin.readline())
budget = list(map(int, stdin.readline().split()))
total_budget = int(stdin.readline())

def solution(num, budget, total_budget):
    result = 0
    # 배정될 예산을 이분 탐색의 범위로 잡음
    left, right = 0, max(budget)

    while left <= right : # left가 rigit보다 커진것만 아니면
        sum_budget = 0
        mid = (left + right) // 2

        for x in budget :
            sum_budget += min(mid, x)
        # print(left, mid, right, sum_budget)
        
        # 계산한 예산이 배정된 예산을 넘으면 => 더 적은 예산으로 배정해야 함
        if sum_budget > total_budget :
            right = mid - 1
        # 계산한 예산이 배정된 예산보다 적으면 => 더 많은 예산을 배정할 수 있음
        else :
            left = mid + 1
        
        result = right
        
    return result


print(solution(num, budget, total_budget))
