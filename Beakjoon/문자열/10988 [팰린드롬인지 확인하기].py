from sys import stdin

input = stdin.readline

word = input().strip()
re_word = "".join(reversed(word))

if word == re_word :
    print(1)
else : print(0)

# print(int(word==word[::-1]))