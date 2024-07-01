"""
문제
* 정상적인 괄호 표기면 True, 아니면 False

권장 시간복잡도
* O(N)

내 풀이
* stack에 데이터를 넣고, top에 있는 데이터와 입력받는 데이터가 상쇄되면 pop, 아니면 push
* pop해야 하는 상황에서 스택에 데이터가 없거나 for문 다 돌았는데 남아있으면 False
"""

def solution(s):
    stack = []
    is_suc = True
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
            continue
        if stack == []:
            is_suc = False
            break
        stack.pop()
    if stack != []:
        is_suc = False

    return is_suc

print(solution('(())()'))
print(solution('((())()'))