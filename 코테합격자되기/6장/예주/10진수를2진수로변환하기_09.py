## 문제 09 10진수를 2진수로 변환하기 

def solution(decimal): 
    # return bin(decimal)
    return format(decimal, 'b')

print(solution(10))

def stack_solution(decimal): 
    stack = [] 
    while decimal > 0: 
        remainder = decimal % 2 
        stack.append(str(remainder))
        decimal //= 2 
    
    answer = ""
    while stack:  ## stack에 값이 있으면 true
        answer += stack.pop()
    return answer

## decimal이 1이 될떄까지 계속 2로 나누므로 시간복잡도는 O(logN)
    
        
        
print(stack_solution(1))