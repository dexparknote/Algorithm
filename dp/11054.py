# 가장 긴 바이토닉 부분 수열
# 바이토닉 수열 -> 10, 20, 30, 25 ,20 즉, 10 < 20 < 30 > 25 > 20
# 예제) 1 5 2 1 4 3 4 5 2 1 -> 1 2 3 4 5 2 1 길이는 7
n = int(input())
a = list(map(int,input().split()))
dp = [1] * n
dp2 = [1] * n
result = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(n-1,0,-1):
    for j in range(n-1,0,-1):
        if a[i] > a[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

for i in range(n):
    result[i] = dp[i] + dp2[i] -1

print(max(result))

