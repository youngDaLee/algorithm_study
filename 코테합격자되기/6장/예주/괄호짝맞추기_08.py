## 06-3몸풀기 문제 
## 문제 08 괄호 짝 맞추기 

def solution(s): 
    stack = [] 
    for char in s: 
        if char == "(": 
            stack.append(char)
        elif char == ")": 
            if len(stack) <= 0: 
                return False 
            else: 
                stack.pop()
    
    ## for문 모두 순회 
    if len(stack) == 0: 
        return True 
    else: 
        return False
    
    
    
print(solution("(())"))
print(solution("(()))"))
print(solution("("))
