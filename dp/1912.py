# 연속합
# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하자.
# 10,-4,3,1,5,6,-35,12,21,-1 -> 12+21=33 이 정답
n = int(input())
a = list(map(int, input().split()))
for i in range(1,n):
    a[i] = max(a[i], a[i-1]+a[i])
print(max(a))
print(a)


