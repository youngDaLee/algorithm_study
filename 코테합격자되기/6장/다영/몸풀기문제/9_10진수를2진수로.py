"""
문제
* 10진수를 2진수로 변환해 반환

권장 시간복잡도
* O(logN)

내 풀이
* 10진수 -> 2진수 변환 방법
    * 10진수 N을 2로 나눈 나머지를 저장하고, N을 2로 나눔
    * 몫이 0일 때 까지 반복, 모든 과정이 끝나고 저장한 나머지를 역순으로 붙임
* 나머지를 스택에 저장, 나누기 반복 -> 끝나고 스택 그대로 출력
"""

def solution(num):
    stack = []
    while num > 0:
        rest = num % 2
        num = num//2
        stack.append(rest)

    binary = ''
    while stack:
        binary += str(stack.pop())
    return binary

print(solution(13))