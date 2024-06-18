from collections import deque
import copy

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    # 원래의 graph는 유지시킴
    tmp_graph = copy.deepcopy(graph)

    # 바이러스를 큐에 넣음
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

        # 탐색 시작
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위 확인
                continue
            if tmp_graph[nx][ny] == 0:  # 감염 퍼뜨리기
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)


def makewall(cnt):
    # 벽 3개가 세워지면 바이러스를 퍼뜨려 봄
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:  # 빈 공간에 벽 세우기
                graph[i][j] = 1
                makewall(cnt + 1)  # 다시 두번째 벽 세우기
                graph[i][j] = 0  # 다시 벽을 허무는 과정 (백트래킹)


for i in range(n):
    graph.append(list(map(int, input().split())))
answer = 0
makewall(0)
print(answer)