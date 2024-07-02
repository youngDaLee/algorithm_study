'''
N명의 사람들이 원 형태로 서 있습니다. 각 사람은 1부터 N까지 번호표를 갖고 있습니다. 그리고
임의의 숫자 K가 주어졌을 때 다음과 같이 사람을 없앱니다

• 1번번호표를가진사람을기준으로K번째사람을없앱니다.
• 없앤사람다음사람을기준으로하고다시K번째사람을없앱니다. 

1 <= N,K <= 1000

=== 


'''
from collections import deque

def solution(n,k): 
    queue = deque(range(1, n+1)) 
    
    while len(queue) > 1: # 1명 남을때까지 반복한다. 
        # k만큼 queue popleft 수행하고 queue에 push 한다 
        for i in range(1,k): 
            element = queue.popleft()
            queue.append(element)
        queue.popleft()
    return queue[0]

print(solution(5,2))
            
        
    
    
solution(5,2)