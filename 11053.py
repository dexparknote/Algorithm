# 수열 A = {10,20,10,30,20,50} 인 경우 가장 긴 증가하는 부분 수열은
# 10,20,30,50이고 길이는 4이다.
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
        