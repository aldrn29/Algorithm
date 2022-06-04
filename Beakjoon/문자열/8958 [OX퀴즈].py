from sys import stdin

input = stdin.readline

num = int(input())
for _ in range(num) :
    ox = input().strip()
    score = 0
    prev = 1

    for i in range(len(ox)) :
        if ox[i] == 'O' :
            score += prev
            prev += 1
        else :
            prev = 1 
            continue
    print(score)
