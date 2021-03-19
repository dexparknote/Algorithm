# 계단 오르기
# 10 20 15 25 10 20 계단 점수
# 규칙
# 1. 한 게단 씩 또는 두 계단씩 오를 수 있음
# 2. 연속된 세 개의 계단을 모두 밟아서 안됨.
# 3. 마지막 계단 반드시 밟아야 함.

n = int(input())
s = []
dp = [0] * n
for i in range(n):
    s.append(int(input()))

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1]+s[2], s[0]+s[2])

for i in range(3, n):
    dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
print(dp[n-1])

