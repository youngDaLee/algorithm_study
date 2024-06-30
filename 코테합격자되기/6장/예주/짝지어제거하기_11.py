## 짝지어 계산하기 
## 괄호 문제랑 동일하게 풀면 될듯 

def solution(str): 
    stack = [] 
    for char in str: 
        
        if len(stack) > 0 and stack[-1] == char: 
            stack.pop()
        else: 
            stack.append(char)
            
    if stack: 
        return 0 
    else: 
        return 1
    
    
print(solution("baabaa"))
print(solution("cdcd"))