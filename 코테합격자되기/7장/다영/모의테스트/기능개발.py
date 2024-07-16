"""
문제
* 각 기능은 진도가 100%일 때 서비스 반영 가능
* 뒤의 기능은 앞의 기능이 배포될 때 함께 배포되어야 함
* 각 배포마다 몇 개 기능이 배포되는지
* 제약사항
    * len(progresses) == len(speeds)

권장 시간복잡도
* O(N)

내 풀이
* days는 0에서 시작
* top에 있는 수가 100이 될 때 까지 days를 늘림
* top(progress) + top(speeds)*days >= 100 이면 해당 조건에 맞는 데이터 나올 때 까지 queue를 pop, cnt를 ++
* 조건 안 맞으면 cnt를 초기화 하고 days를 다시 조건 맞을 때 까지 늘림
"""
from collections import deque


def solution(progress, speeds):
    progress = deque(progress)
    speeds = deque(speeds)

    days = 0
    cnt = 0
    res = []
    while progress:
        while (progress[0]+speeds[0]*days < 100):
            days += 1

        while (progress and progress[0]+speeds[0]*days >= 100):
            progress.popleft()
            speeds.popleft()
            cnt += 1

        res.append(cnt)
        cnt = 0

    return res


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))