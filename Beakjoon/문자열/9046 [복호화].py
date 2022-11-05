n = int(input())
s = [input().strip() for _ in range(n)]

for x in s :
    dic = dict()

    for c in x :
        if c == ' ': continue
        if c in dic :
            dic[c] += 1
        else : dic[c] = 1

    '''
    max_key = ''
    max_value = 0
    count = 0

    for key, value in dic.items() :
        if value > max_value :
            max_value = value
        
    for key, value in dic.items() :
        if value == max_value :
            count += 1
            max_key = key 

    if count > 1 : print('?')
    else : print(max_key)
    '''

    cnt = list(dic.items())
    cnt.sort(key = lambda x : -x[1])

    if len(cnt) > 1 and cnt[0][1] == cnt[1][1] :
        print('?')
    else :
        print(cnt[0][0])