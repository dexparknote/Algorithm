# 가장 긴 바이토닉 부분 수열
# 바이토닉 수열 -> 10, 20, 30, 25 ,20 즉, 10 < 20 < 30 > 25 > 20
# 예제) 1 5 2 1 4 3 4 5 2 1 -> 1 2 3 4 5 2 1 길이는 7
n = int(input())
a = list(map(int,input().split()))
dp1 = [1] * n
dp2 = [1] * n
result = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

a.reverse()

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

dp2.reverse()

for i in range(n):
    result[i] = dp1[i] + dp2[i]

print(max(result)-1)

