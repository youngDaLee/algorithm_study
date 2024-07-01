"""
문제
* 주식 가격 price가 주어질 때, 떨어지지 않은 기간은 몇 초인지 반환

권장 시간 복잡도
* O(N)

나의 풀이
* price를 순회
* 값이 크면 push
* 작은 값이 나오면 그것보다 작은 값 나올 때 까지 pop, pop한만큼 cnt+
* 더한 cnt를 

배운점
* 구현이 어려우면 일단 구현해보자 효율성 따지지 말고 
"""

def 일단구현_solution(prices):
    res = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        res.append(cnt)

    return res

def solution(prices):
    res = [0] * len(prices)

    stack = [0]
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        res[j] = (len(prices)-1) - j

    return res

print(일단구현_solution([1, 2, 3, 2, 3]))
print(solution([1, 2, 3, 2, 3]))
