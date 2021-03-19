# 가장 큰 수 (프로그래머스)
# lamda를 잘 쓰면 좋을꺼같다!
numbers = [3, 30, 34, 5, 9]
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    return str(int(''.join(numbers)))
print(solution(numbers))
