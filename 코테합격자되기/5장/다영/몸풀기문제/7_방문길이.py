"""
문제
* U: 위로한칸 / D: 아래쪽으로 한 칸 / R: 오른쪽으로 한 칸 / L: 왼쪽으로 한 칸
* 게임 캐릭터가 처음 지나간 길의 길이
* 가로 +-5, 세로 +-5 그래프

권장 시간복잡도
* O(N)

내 풀이]
* 처음생각
    * visit 그래프를 구하고, 해당 그래프에 방문했으면 True로 표기
    * 처음 방문한 경우만 +1
    * 노드가 아니라 간선을 기준으로 생각해야 해서 pass...
* 고친 생각
    * visit 그래프를 간선으로 만들기
    * 오는거/가는거 표시하는 방법도 있지만 메모리 낭비라 생각 -> 규칙을 정하기
        * 가로의 경우 왼쪽 정점이 앞에 오도록
        * 세로의 경우 위쪽 정점이 앞에 오도록

"""
def move(flag, node):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    x = node[0]
    y = node[1]

    if flag == 'U':
        idx = 0
    elif flag == 'D':
        idx = 1
    elif flag == 'R':
        idx = 2
    elif flag == 'L':
        idx = 3

    return x+dx[idx], y+dy[idx]


def is_valid_range(node):
    return -5 <= node[0] <=5 and -5 <= node[1] <=5


def make_visit():
    nodes = []
    for x in range(-5, 6):
        for y in range(-5, 6):
            nodes.append((x,y))

    visit={}
    for node in nodes:
        left = move('L', node)
        up = move('U', node)

        if is_valid_range(left):
            visit[(left, node)] = False
        if is_valid_range(up):
            visit[(up, node)] = False

    return visit


def make_key(dir, node, next_node):
    if dir in ['L', 'U']:
        return (next_node, node)
    else:
        return (node, next_node)


def solution(dirs):
    node = (0, 0)
    visit = make_visit()
    ans = 0
    for dir in list(dirs):
        next_node = move(dir, node)
        if not is_valid_range(next_node):
            continue

        key = make_key(dir, node, next_node)
        if not visit[key]:
            visit[key] = True
            ans += 1

        node = next_node

    return ans

print(solution('LULLLLLLU'))