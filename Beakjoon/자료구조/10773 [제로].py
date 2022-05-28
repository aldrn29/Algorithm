import sys 
input = sys.stdin.readline

num = int(input())
st = []

for _ in range(num) :
    n = int(input())

    if n != 0 :
        st.append(n)
    else :
        st.pop()

print(sum(st))