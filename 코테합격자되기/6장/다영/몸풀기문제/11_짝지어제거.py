"""
문제
* 문자열에서 같은 알파벳 2개 붙어있는 짝을 찾고, 짝을 찾으면 제거하고 제거한 자리를 이어붙임
* 문자열 제거가 되면 1, 아니면 0

권장 시간 복잡도
* O(N)

나의 풀이
* s를 순회하면서 stack의 top이랑 같으면 stack을 pop, 아니면 push
* 마지막에 남아있어면 false
"""

def solution(s):
    stack = []
    for st in s:
        if stack and stack[-1] == st:
            stack.pop()
        else:
            stack.append(st)
    if len(stack) > 0:
        return False
    return True
