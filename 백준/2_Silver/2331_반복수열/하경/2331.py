A, P = map(int, input().split(" "))
D = []
D.append(A)
print(A, P)
print(D)
i = 0  # iteration
print(D[i])


while(True):
    if D[i] > 100:
        next = ((D[i] // 100) % 10) ** P  # 100의 자리
        + ((D[i] // 10) % 10) ** P  # 10의 자리
        + (D[i] % 10) ** P  # 1의 자리

    if D[i] < 100:
        next = ((D[i] // 10) % 10) ** P  # 10의 자리
        + (D[i] % 10) ** P  # 1의 자리


    if next in D: # 반복수열 탐색
        index = D.index(next) # 처음 나오는 인덱스 반환
        D = D[:index]
        break
    i += 1

print(len(D))
