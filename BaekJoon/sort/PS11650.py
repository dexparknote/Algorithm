n = int(input())
result = []
for i in range(n):
    [a, b] = map(int, input().split())
    result.append([a, b])

arr = sorted(result)

for i in range(n):
    print(arr[i][0], arr[i][1])