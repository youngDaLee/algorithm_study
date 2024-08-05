'''
다리 건설 비용 costs
최소 비용으로 모든 섬이 통행하는 solution
'''
def solution(n, costs):
    answer = 0

    # 비용순 정렬
    costs.sort(key=lambda x:x[2])
    island = set([costs[0][0]])

    # 모든 섬 탐색
    while len(island) != n:
        for cost in costs:
            if cost[0] in island and cost[1] in island:
                continue
            # 낮은비용순으로 탐색했을 때 섬이 있으면 더하기
            if cost[0] in island or cost[1] in island:
                island.add(cost[0])
                island.add(cost[1])
                answer += cost[2]
                break

    return answer
