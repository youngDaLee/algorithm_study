def exp(a, result):
    while (True):
        if len(a) < 2:  # 마지막 최댓값에 도달했을 때
            break

        max_num = max(a)  # 최댓값
        idx = a.index(max_num)  # 최댓값의 위치

        for i in a[:idx]:  # 최댓값의 앞부분 값들에 대한 이익
            result += (max_num - i)

        if idx == len(a) - 1:
            break
        a = a[idx + 1:]  # 최댓값의 뒷부분

    print(result)
    result = 0  # 초기화


def main():
    t = int(input())
    result = 0

    for _ in range(0, t):
        p = int(input())
        a = list(map(int, input().split(" ")))

        exp(a, result)

main()