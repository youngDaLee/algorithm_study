a = list(map(int, input().split(" ")))
a_sort = sorted(a)
print("순열 정렬:", a_sort)
print("    순열:", a)

result = [] # 결과 리스트
cycle = []  # 각 사이클
flag = False


# 순열 전체 숫자에 대해 탐색
for i in range(0, len(a)):
    # 해당 숫자가 이미 다른 사이클에 속해 있는지 탐색
    for rst in result:
        if a_sort[i] in rst:
            flag = True
            break
    if flag == True:
        flag = False
        continue

    # 위치 같음 -> 자기 자신 사이클
    if i == a.index(a_sort[i]):
        cycle.append(a_sort[i])

    # 위치 다름 -> Trace 하며 끝까지 찾기
    else:
        cycle.append(a_sort[i])
        cycle.append(a[i])

        while(True):
            i = a_sort.index(a[i])
            if a[i] in cycle: # 사이클 시작점에 도달
                break
            cycle.append(a[i])

    result.append(cycle)
    cycle = [] # 초기화


print("순열 사이클:", result)
print("개수:", len(result))
