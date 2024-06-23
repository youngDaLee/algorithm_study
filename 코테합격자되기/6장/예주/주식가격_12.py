## 주식 가격 
# O(n)

def solution(prices): 
    
    answer = [0] * len(prices)  
    
    stack = [0]
    for i in range(1, len(prices)):
        # 주식이 떨어짐
        
        print(prices[i] < prices[stack[-1]])
        while stack and prices[i] < prices[stack[-1]]: 
            # 가격이 떨어짐
            j = stack.pop()
            answer[j] = i - j
        
        stack.append(i)    
        
        
        # 스택에 남아있는 가격들은 가격이 떨어지지 않은 경우임
    while stack: 
        j = stack.pop() 
        answer[j] = len(prices) - 1 - j 
    return answer 

    
print(solution([1,6,9,5]))
print(solution([1,2,3,2,3]))