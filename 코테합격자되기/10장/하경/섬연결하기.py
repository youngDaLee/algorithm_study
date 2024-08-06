'''
n-1개의 다리들이 필요함.
=> nCn-1 = nC1 = n개의 경우의 수

각 다리 조합에 대하여
1. 해당 조합들이 노드들을 모두 잇는지 확인하고
2. 위 조건을 패스한 조합들의 cost 총합을 구하여 최솟값을 찾는다.
'''
def solution(costs):
    copy = costs # 복제
    for i in range(len(costs)):
        costs.remove(costs[i]) # n-1개의 다리

        print(costs)
        costs = copy # 복제본으로 reassign
    # 각 노드가 연결되었는지 확인
    # 아니라면
    # continue
    #
    # cost
    # 계산 -> 최솟값
    # 반환
    #

n = int(input())
costs = eval(input())
print(solution(costs))