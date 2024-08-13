'''
k 크기의 배열을 만들어 모든 원소를 -1로 초기화함.
Union 연산: 배열의 인덱스 자리에 자기 값을 assign -> 두 노드값을 비교하여, 작은 인덱스 자리에 큰 값을 assign
Find 연산: 재귀함수로 루트노드 찾기
집합 개수 세기: 자기의 값과 부모노드 값이 같다면, 그 놈이 루트 노드(대표 원소)임.
'''
def union(A, B, array):
    array[A] = A
    array[B] = B
    if A > B: # 대소 비교
        array[B] = A
    else:
        array[A] = B

def find(node, array):
    answer = array[node]
    if array[node] == node: # 부모노드 값이 자기 자신이라면 그 놈이 루트노드
        return
    find(answer, array)

def solution(k):
    global array # 전역변수
    array = [-1 * i for i in range(k)]
    count = 0
    while True:
        operation = eval(input())
        if operation[0] == 'u':  # union 연산
            A, B = operation[1:]
            union(A, B, array)
        elif operation[0] == 'f':  # find 연산
            node = operation[1]
            find(node, array)
            break

    for i in range(len(array)):
        if i == array[i]: # 부모노드 값이 자기 자신이라면
            count += 1

    return count


k = int(input())
print(solution(k))



