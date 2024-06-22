"""
문제
* 대괄호, 중괄호, 소괄호로 이루어진 문자열 s
* s를 왼쪽으로 x 만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x 개수

권장 시간 복잡도
* O(N^2)

나의 풀이
* s의 길이만큼 회전시켜가면서 괄호 성립 여부를 확인
"""
bracket_dict = {'{': '}', '(': ')', '[': ']'}

def is_suc_bracket(bracket, top):
    if bracket_dict[top] == bracket:
        return True
    else: return False

def is_bracket(s):
    stack = []
    for bracket in s:
        if bracket in bracket_dict.keys():
            stack.append(bracket)
            continue
        if stack == []: return False
        if is_suc_bracket(bracket, stack[-1]):
            stack.pop()
        else:
            return False
    if stack != []: return False
    return True

def solution(s):
    cnt = 0
    for _ in range(len(s)):
        if is_bracket(s):
            cnt += 1

        s = s[-1] + s[:-1]
    return cnt

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))