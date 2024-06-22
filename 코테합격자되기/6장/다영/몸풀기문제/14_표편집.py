"""
문제
* 표 편집 툴
    * U X : 현재 행 기준 X칸 위의 행을 선택
    * D X : 현재 행 기준 X칸 아래 행을 선택
    * C : 현재 행 삭제 후 아래 행 선택(선택한 행이 가장 마지막이면 바로 윗행 선택)
    * Z : 가장 최근 삭제 행을 복구 -> 현재 선택한 행은 바뀌지 않음
* 모든 명령 수행 후 삭제된 행은 X, 삭제되지 않은 행 O로 표기
* 표 행 개수 n, 행 위치 k, 수행 명령 cmd

시간복잡도
* O(N)

풀이
* 현재 위치를 저장하는 k
* 표 길이 만큼의 삭제 표시 여부 list
* 삭제된 행을 stack에 저장, 삭제 시 O->X
* 복구 시 stack 최상단의 인덱스를 X->O
"""

def solution(n, k, cmd):
    stack = []
    del_li = ['O'] * n
    for c in cmd:
        if c == 'C':
            del_li[k] = 'X'
            k = k+1 if k<(n-1) else k-1
            stack.append(k)
        elif c == 'Z':
            idx = stack.pop()
            del_li[idx] = 'O'
        else:
            ud, x = map(str, c.split(" "))
            if ud == 'U': k -= int(x)
            elif ud == 'D': k += int(x)
        print(k, c)
    return "".join(del_li)

print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))