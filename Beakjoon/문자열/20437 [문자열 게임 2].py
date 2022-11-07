import re
from collections import defaultdict

num = int(input())

for _ in range(num) :
    w = input().strip()
    k = int(input())

    '''
    dic = {}
    result = []

    for s in w :
        if s in dic :
            dic[s] += 1
        else : dic[s] = 1

        # 어떤 문자가 k개 있다면
        if dic[s] == k :
            temp = []
            for f in re.finditer(s, w) :
                temp.append(f.start())

            result.append(temp[k-1] - temp[0] + 1)

    if len(result) > 0 :
        print(min(result), max(result))
    else : print(-1)
    '''

    # 시간초과
    '''
    result = []
    for i in range(len(w)) :
        if w[i] in w[i+1:] :
            count = 1
            for j in range(i+1, len(w)) :
                if w[i] == w[j] :
                    count += 1
                if count == k :
                    result.append(j-i+1)
                    break

    if len(result) > 0 :
        print(min(result), max(result))
    else : print(-1)
    '''

    alpha = defaultdict(list)
    for i in range(len(w)) :
        if w.count(w[i]) >= k :
            alpha[w[i]].append(i)


    if alpha :
        result = []
        for alpha_list in alpha.values() :
            # print(alpha_list)
            for i in range(len(alpha_list)-k+1) :
                result.append(alpha_list[i+k-1] - alpha_list[i] + 1)

        print(min(result), max(result))
    else :
        print(-1)