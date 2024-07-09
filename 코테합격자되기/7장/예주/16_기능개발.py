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

    answer = []
    progress_queue = deque(progresses)
    speeds_queue = deque(speeds)
    
    time = 0
    count = 0
    
    while len(progress_queue) > 0: 
        if (progress_queue[0] + time * speeds_queue[0]) >= 100:  ## 종료 가능한지 확인 
            progress_queue.popleft()
            speeds_queue.popleft()
            count += 1 
        else: 
            if count > 0:
                answer.append(count)
                count = 0
            time += 1 
            
    answer.append(count)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))