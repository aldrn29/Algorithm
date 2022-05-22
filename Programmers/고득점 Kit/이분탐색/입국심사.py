# n : 기다리는 사람
# times : 한 명 심사에 걸리는 시간
def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left, right = 1, max(times) * n

    return answer


print(solution(6, [7, 10]))
