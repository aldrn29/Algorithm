from collections import deque
from sys import stdin

num = int(stdin.readline())
card = deque([i for i in range(1, num+1)])

while card :
    if len(card) == 1 : 
        result = card.popleft()
        print(result)
        break

    card.popleft()

    if card :
        card.rotate(-1)