# 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8}
# 합이 가장 큰 증가 부분 수열은 1,2,50,60 이고, 합은 113이다.
n = int(input())
a = list(map(int,input().split()))
dp = [i for i in a] #초기화는 입력받은 값으로 로직은 맞았으나 리스트 초기화 문제였음.
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+a[i])
print(max(dp))

