# n : 기다리는 사람
# times : 한 명 심사에 걸리는 시간
def solution(n, times):
    answer = 0

    # 걸리는 시간을 이분 탐색의 범위로 잡음
    left, right = 1, max(times) * n

    while left < right :
        num = 0
        mid = (left + right) // 2
        print(left, mid, right)

        for x in times :
            num += mid // x
        
        # 심사한 사람의 수가 기다리는 사람보다 많으면 => 더 적은 시간으로 심사할 수 있음
        if num >= n :
            right = mid
        # 심사한 사람의 수가 기다리는 사람보다 적으면 => 더 많은 시간이 필요함
        elif num < n :
            left = mid + 1

        answer = left
    return answer


print(solution(6, [7, 10]))
