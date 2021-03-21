# H-Index
# 테스트 케이스 1은 맞았지만 런타임 에러가 뜬다..
citations = [3,0,6,1,5]

def solution(citations):
    n = sum(citations)//len(citations)
    citations.sort()
    sum1 = 0
    sum2 = 0
    for i in citations:
        if i >= citations[n-1]:
            sum1 = sum1 + 1
        else:
            sum2 = sum2 + 1
    
    return max(sum1,sum2)

print(solution(citations))
