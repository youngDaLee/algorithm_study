"""
문제
* N까지의 번호표, K가 주어졌을 때 아래와 같은 방식으로 사람 없앰
    * 1번 번호표 가진 사람 기준 K번째 사람 없앰
    * 없앤 사람 기준 K번째 사람 없앰

권장 시간복잡도
* O(N*K)

내 풀이
* k까지 popleft, push / k번째는 push안하고 없앰
* 이 과정 반복
"""
from collections import deque

def solution(n, k):
    q = deque([i for i in range(1, n+1)])
    while q:
        for _ in range(k-1):
            q.append(q.popleft())
        now = q.popleft()
    return now

print(solution(5,2))
