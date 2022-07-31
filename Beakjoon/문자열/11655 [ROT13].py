str = input()
rot13 = ''

for s in str :
    if 'a'<= s <= 'z' :
        s = ord(s) + 13
        if s > ord('z') :
            s -= 26
        rot13 += chr(s)
    elif 'A'<= s <= 'Z' :
        s = ord(s) + 13
        if s > ord('Z') :
            s -= 26
        rot13 += chr(s)
    else :
        rot13 += s

print(rot13)
