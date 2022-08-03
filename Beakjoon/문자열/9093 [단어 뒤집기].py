num = int(input())

for _ in range(num) :
    str = input().split()

    for s in str :
        print(''.join(reversed(s)), end=' ')
    print()

# import sys
# myr = sys.stdin.readline
# for _ in range(int(myr())):
#     tmp = list(myr().split())
#     for i in tmp:
#         print(i[::-1], end = ' ')