# 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8}
# 합이 가장 큰 증가 부분 수열은 1,2,50,60 이고, 합은 113이다.
n = int(input())
a = list(map(int,input().split()))
dp = [1 for _ in range(n)]
dp[0] = a[0]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+a[i])
print(dp)


