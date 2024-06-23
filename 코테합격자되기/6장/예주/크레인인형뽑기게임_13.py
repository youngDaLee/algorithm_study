# 문제13 크레인인형뽑기

def solution(board, moves):
    answer = 0
    stack = list()
    
    
    while moves:
        now = moves.pop(0) - 1 
        
        for line in board:
            
            if line[now] != 0:
                stack.append(line[now])
                line[now] = 0
                
                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                        
                break  
                        
    return answer
    
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
               [1,5,3,5,1,2,1,4]))
