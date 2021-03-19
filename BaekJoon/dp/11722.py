# 가장 긴 감소하는 부분 수열
# 수열 A = {10,30,10,20,20,10}인 경우에 가장 긴 감소하는 부분 수열 30,20,10 이고, 길이 3
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))