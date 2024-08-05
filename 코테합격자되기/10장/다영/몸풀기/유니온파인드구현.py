'''
union(x, y) : x, y가 속한 두 집합을 합침
find(x) : x가 속한 집합의 대표 원소를 찾음

초기의 노드는 부모 노드를 자신의 값으로 설정했다고 가정
여기서는 각 집합의 루트노드를 기준으로 루트노드가 작은 노드를 더 큰 노드의 자식으로 연결한는 방법 사용
'''

def find(parents, x):
    # 루트 찾기 함수
    if parents[x] == x: # 만약 x의 부모가 자기 자신, 즉 x가 루트노드면
        return x
    # 그렇지 않으면 x의 부모를 찾아서 parent[x]에 저장
    # 그 부모노드의 루트노드를 찾아 parent[x]에 저장
    parents[x] = find(parents, parents[x])
    return parents[x] # parents[x]를 반환


def union(parents, x, y):
    # 두 개의 집합을 합치는 함수
    root1 = find(parents, x) # x집합 루트 노드 찾기
    root2 = find(parents, y) # y집합 루트 노드 찾기

    parents[root2] = root1

def solution(k, operations):
    parents = list(range(k)) # 처음에는 각 노드가 자기 자신을 부모로 가지도록 초기화
    n = k # 집합 개수를 저장할 변수

    for op in operations:
        if op[0] == 'u':
            union(parents, op[1], op[2])
        elif op[0] == 'f':
            find(parents, op[1])

    n = len(set(find(parents, i) for i in range(k)))

    return n
