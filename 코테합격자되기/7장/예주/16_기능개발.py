'''

배포 순서대 로 작업 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌정수 배열 speeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 반환하도록 solution( ) 함수를 완성하세요.

• 작업개수(progresses,speeds의배열길이)는100개이하입니다.
• 작업진도는100미만의자연수입니다.
• 작업속도는100이하의자연수입니다.
• 배포는하루에한번만할수있으며,하루의끝에이루어진다고가정합니다.예를들어진도
율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

[93, 30, 55] [1, 30, 5] [2, 1]
[95, 90, 99, 99, 80, 99] [1, 1, 1, 1, 1, 1] [1, 3, 2]

=== 


'''

from collections import deque
def solution(progresses, speeds):
    # progresses에서 하나 빼와서 -> 작업이 완료될때까지 반복 
    day = 0
    answer = []
    while progresses: # 남은 작업이 없을때까지 수행
        current_progress = progresses.pop(0)
        current_speed = speeds.pop(0)
        
        while current_progress < 100:  #100% 이상 될때까지 수행
            day += 1  
            current_progress += current_speed
        answer.append(day)
        
    
    return answer

print(solution([93, 30, 55],[1, 30, 5]))