"""
문제
* N*N 크기의 board
* board 에서 인형을 집어 바구니에 담을 수 있음
* 인형이 들어와서 같은 모양 인형이 연속으로 쌓이면 터짐
* 작동시킨 후 사라진 인형 개수를구하기

풀이
* moves에서 크레인 인형을 pop해옴
* pop한 인형을 bucket에 넣음 -> top과 같으면 pop 후 cnt 더하기
"""

def solution(board, moves):
    bucket = []
    cnt = 0
    for move in moves:
        move -= 1 # 헷갈리니까 인덱스 기준으로..
        doll = 0
        while board[move] and doll == 0:
            doll = board[move].pop()
        if doll == 0:
            continue

        if bucket and bucket[-1] == doll:
            bucket.pop()
            cnt += 2
        else:
            bucket.append(doll)

    return cnt


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
