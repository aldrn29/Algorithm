# yellow로 나올 수 있는 경우의 수 계산
# (가로길이, 세로길이) = (1,24), (2,12), (3,8), (4,6), (6,4), ... (24, 1)

# yellow 카펫의 가로길이가 세로길이보다 큰 경우에서
# 테두리를 감싸는데 필요한 양 = brown 이라면
# 전체 카펫의 크기 return

# 시간 초과
def solution_legacy(brown, yellow):
    answer = []
    yellow_list = []

    for x in range(yellow, 0, -1) :
        for y in range(1, yellow+1) :
            if x < y : continue

            if x * y == yellow :
                yellow_list.append((x, y))
                break

    for x, y in yellow_list :
        if x*2 + y*2 + 4 == brown : 
            answer.append(x+2)
            answer.append(y+2)

    return answer

# 개선 코드
def solution(brown, yellow):
    total = brown + yellow

    for x in range(total, 2, -1) :  # 가로
        # 약수 찾기
        if total % x == 0 :
            y = total // x
            
            if (x-2) * (y-2) == yellow :
                return [x, y]

print(solution(24, 24))