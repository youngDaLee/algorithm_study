def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char: # 같은 문자가 붙어있으면 pop
            stack.pop()
        else:
            stack.append(char) # 비었거나 문자가 서로 다르면 append

    if stack:
        return 0
    else:
        return 1


s = input()
print(solution(s))