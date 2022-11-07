import re
from sys import stdin
input = stdin.readline

str = input().strip()
p = re.compile('<[a-zA-Z0-9 ]+>|[a-zA-Z0-9 ]+')
words = p.findall(str)
result = ''

for word in words :
    if word[0] == '<' :
        result += word
    else :
        if ' ' in word :
            s = word.split()
            for i in range(len(s)) :
                result += ''.join(reversed(s[i]))
                if i != len(s)-1 : result += ' '
        else :
            result += ''.join(reversed(word))

print(result)