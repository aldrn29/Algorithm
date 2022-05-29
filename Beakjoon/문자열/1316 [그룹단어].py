from sys import stdin
input = stdin.readline

'''
result = 0
for i in range(int(input())) :
    word = input()
    if list(word) == sorted(word, key=word.find) :
        result += 1

print(result)
'''

num = int(input())
result = num

for i in range(num) :
    word = list(input())

    for s in range(len(word)-1) :
        if word[s] == word[s+1] :
            continue
        elif word[s] in word[s+1:] :
            result -= 1
            break

print(result)
