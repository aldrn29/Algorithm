h, m, s = map(int, input().split(':'))
t_h, t_m, t_s = map(int, input().split(':'))

# 모두 초로 바꾸고 빼기
prev = (h * 3600) + (m * 60) + s
targ = (t_h * 3600) + (t_m * 60) + t_s

if prev >= targ : 
    prev = (24 * 3600) - prev
    result = targ + prev
else :
    result = targ - prev

time = []
for _ in range(2) :
    temp = result % 60
    time.append(temp)
    result = result // 60
time.append(result)

time = time[::-1]
time = [str(x).zfill(2) for x in time]
print(':'.join(time))

