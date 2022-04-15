import sys

n = int(input())
data = [sys.stdin.readline().strip() for _ in range(n)]

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 중복제거

data = list(set(data))
data.sort()
data.sort(key=len)
print(data)
for i in data :
    print(i)

