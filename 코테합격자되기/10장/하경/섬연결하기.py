'''
===다영이 솔루션 복붙해옴===
사실 집합 문제라기보단 Brute Force 같다고 함.
costs 리스트를 처음부터 탐색하고 또 처음부터 탐색하고, ... 이 과정을 island 요소 개수가 n이 될 때까지 반복하는 작업
------->
---------------->
... (반복) ...
------------------------->
[[0,1,1], [1,3,1], [0,2,2], [1,2,5], [2,3,8]]
'''
def solution(n, costs):
    answer = 0

    # 비용순 정렬
    costs.sort(key=lambda x:x[2])
    island = set([costs[0][0]]) # 첫번째 섬
    print(costs)
    # 모든 섬 탐색
    while len(island) != n: # 모든 섬들이 이어지면 종료
        # 각 브릿지별 탐색
        for cost in costs:
            print(answer)
            if cost[0] in island and cost[1] in island: # 두 섬들이 이미 island에 포함되어 있다면
                continue
            # 낮은 비용순으로 탐색했을 때 섬이 있으면 더하기
            if cost[0] in island or cost[1] in island: # 두 섬 중에 하나가 이미 island에 포함되어 있다면
                island.add(cost[0])
                island.add(cost[1])
                answer += cost[2]
                break

    return answer

n = int(input())
costs = eval(input())
print(solution(n, costs))