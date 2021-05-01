def solution(participant, completion):
    dic = dict()

    for p in participant:
        dic[p] = dic.get(p, 0) + 1

    # 완주자 목록에 있으면 참가자 목록 인원수 줄이기
    for c in completion:
        dic[c] = dic.get(c) - 1

    for p in participant:
        if dic.get(p) > 0:
            return p

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))