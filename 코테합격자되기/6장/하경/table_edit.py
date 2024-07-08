def solution(n, k, cmd):
    # ➊ 삭제된 행의 인덱스를 저장하는 리스트
    deleted = [ ]
    # ➋ 링크드리스트에서 각 행 위아래의 행의 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)] # 기준이 맨 위일 때를 고려하여 가상 공간 만들기
    down = [i + 1 for i in range(n + 1)] # 기준이 맨 아래일 때를 고려하여 가상 공간 만들기
    # ➌ 현재 위치를 나타내는 인덱스
    k += 1

    # ➍ 주어진 명령어(cmd) 리스트를 하나씩 처리
    for cmd_i in cmd:
        # ➎ 현재 위치를 삭제하고 그다음 위치로 이동
        if cmd_i.startswith("C"):
            deleted.append(k) # 삭제된 요소의 인덱스 따로 보관
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k] # 맨 마지막 행을 삭제했다면 바로 윗 행 선택
        # ➏ 가장 최근에 삭제된 행을 복원
        elif cmd_i.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        # ➐ U 또는 D를 사용해 현재 위치를 위아래로 이동
        else:
            action, num = cmd_i.split()
            if action == "U":
                for _ in range(int(num)): # 숫자만큼 이동
                    k = up[k]
            else:
                for _ in range(int(num)): # 숫자만큼 이동
                    k = down[k]

    # ➑ 삭제된 행의 위치에 'X'를, 그렇지 않은 행의 위치에 'O'를 포함하는 문자열 반환
    answer = ["O"] * n
    for i in deleted:
        answer[i - 1] = "X"


    return "".join(answer)


print(solution(8, 2, ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z']))
print(solution(8, 2, ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z', 'U 1', 'C']))