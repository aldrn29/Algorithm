from itertools import permutations

def solution(numbers):
    answer = []
    pmt = []
    result = []

    for i in range(1, len(numbers)+1) :
        pmt.extend(list(permutations(numbers, i)))

    for i in pmt :  # 각 튜플 원소를 합침
        result.append(int(''.join(x for x in i)))
    result = list(set(result)) # 중복 제거

    # 소수인지 검사
    for x in result :
        if x == 0 or x == 1 : continue
        isPrime = True
        for i in range(2, x) :
            if x % i == 0 : 
                # 소수가 아님
                isPrime = False
                break
        # 소수임
        if isPrime : 
            answer.append(x)

    return len(answer)

print(solution("011"))