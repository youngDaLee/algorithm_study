'''
한 라운드를 올라갈 때마다 각 선수들의 번호는 Ceiling(n/2)가 됨.
같은 매치에서 만나는 플레이어들은 Ceiling(n/2)이 동일함.
'''
import math

def solution(n, a, b):
    count = 1

    while True:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if a == b: # 같은 매치에서 만남
            break

        count += 1

    return count

N, A, B = map(int, input().split(" "))
print(solution(N, A, B))