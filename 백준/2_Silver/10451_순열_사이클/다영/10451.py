import sys
sys.setrecursionlimit(10000)


def dfs(li, visit, i):
    visit[i] = True
    next_i = li[i]
    if not visit[next_i]:
        dfs(li, visit, next_i)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        li = [0] + list(map(int, input().split()))
        visit = [False] * (n+1)
        cycle = 0
        for i in range(1, len(li)):
            if not visit[i]:
                dfs(li, visit, i)
                cycle += 1
        print(cycle)

main()