result = True

def dfs(graph, check, v, bi):
    global result
    if check[v] == 0:
        check[v] = bi
    else:
        if check[v] != bi:
            result = False
        return

    nodes = graph[v]
    new_bi = 2 if bi == 1 else 1
    for node in nodes:
        dfs(graph, check, node, new_bi)


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