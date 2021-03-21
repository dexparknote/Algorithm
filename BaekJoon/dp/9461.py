# 파도반 수열
n = int(input())
for i in range(n):
    dp = [0,1,1,1]
    k = int(input())
    for j in range(4,k+1):
        dp.append(dp[j-3] + dp[j-2])
    print(dp[k])


