# 가장 큰 수 (프로그래머스)
# 내가 푼 풀이 -> 시간 초과로 실패 하지만, 테스트 케이스는 맞음!
numbers = [3, 30, 34, 5, 9]
def solution(numbers):
    temp = 0
    answer = ''
    n = len(numbers)

    numbers = list(map(str, numbers))

    for i in range(n):
        for j in range(i):
            if int(numbers[i][:1]) > int(numbers[j][:1]):
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
        
    for i in range(n):
        answer += numbers[i]

    return answer
print(solution(numbers))
