'''
음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다.
게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,
처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요.
단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.


N	A	B	answer
8	4	7	3 

1 2 3 4 5 6 7 8 
 1   2   3   4  -> current 
   1       2   -> current 
       1  -> current 
       
       

       
       

'''
import math 

print(round(1/2))
print(round(2/2))

def solution(n,a,b): # 4 7  
    answer = 0
    while a != b:     
        answer += 1
        a = math.ceil(a/2) # 2  1 
        b = math.ceil(b/2) # 4  2 
         
        n /= 2
        print(a,b)
        
    return answer
            
        

print(solution(8,1,2)) 