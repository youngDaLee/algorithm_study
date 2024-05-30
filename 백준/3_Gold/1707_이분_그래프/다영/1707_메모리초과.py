import sys
sys.setrecursionlimit(10**6)

def dfs(graph, check, v, group):
    check[v] = group
    for node in graph[v]:
        if check[node] == 0: # 방문하지 않은 노드 탐색
            result = dfs(graph, check, node, -group)
        else:
            result = check[node] == -group
        if not result:
            return False

    return True


def is_graph():
    global result
    result = True
    v, e = map(int, input().split())
    graph = {i: [] for i in range(1, v+1)}
    check = [0] * (v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    dfs(graph, check, 1, 1)

    if result:
        print("YES")
    else:
        print("NO")


def main():
    k = int(input())
    for _ in range(k):
        is_graph()

main()