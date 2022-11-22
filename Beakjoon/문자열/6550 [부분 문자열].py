

# t 를 순회하면서 s를 만들 수 있는지 확인
def check(s, t) :
    s = list(s)
    for i in reversed(t) : 
        if s[-1] == i :
            s.pop()
            if not s :
                print("Yes")
                return 
        else :
            continue
    print("No")
    return

while True :
    try :
        s, t = input().split()
        check(s, t)
    except :
        break