str = input().strip()

for s in str :
    # if 'a' <= s <= 'z' :
    if s.islower() :
        print(s.upper(), end='')
    else : print(s.lower(), end='')

# print(input().swapcase())