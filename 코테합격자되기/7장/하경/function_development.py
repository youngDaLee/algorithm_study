from collections import deque
import math

def solution(progress, speed):
    q = deque()
    q_res = deque()
    pre = 0
    count = 0

    for idx, val in enumerate(progress):
        q.append(math.ceil((100 - val) / speed[idx])) # 각 진도의 남은 일수

    while(q):
        if q[0] > pre: # q[0]과 q.popleft()는 똑같은 값. 맨 앞 기능보다 작업 일수가 오래 걸리면 배포를 나눠준다.
            if count != 0: # 최초 탐색은 제외
                q_res.append(count)
            count = 1
            pre = q.popleft()
        else:
            q.popleft()
            count += 1

        if not q: # 마지막 기능일 때
            q_res.append(count)

    return q_res


progress = list(map(int, input().split()))
speed = list(map(int, input().split(" ")))

print(solution(progress, speed))