from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


n, m = map(int, input().split())
graph = []
wall_spot = deque()
for i in range(n):
    li = list(map(int, input().split()))
    graph.append(li)
    # 점 검사
    for j in range(m):
        if li[j] == 0:
            # 벽 세울 수 있는 점 추가
            wall_spot.append((j,i))


def bfs(graph):
    while wall_spot:
        x, y = wall_spot.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not graph[ny][nx]:
                graph
