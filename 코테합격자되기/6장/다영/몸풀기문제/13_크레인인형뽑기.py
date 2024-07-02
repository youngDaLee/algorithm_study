"""
문제
* N*N 크기의 board
* board 에서 인형을 집어 바구니에 담을 수 있음
* 인형이 들어와서 같은 모양 인형이 연속으로 쌓이면 터짐
* 작동시킨 후 사라진 인형 개수를구하기

풀이
* moves에서 크레인 인형을 pop해옴
* pop한 인형을 bucket에 넣음 -> top과 같으면 pop 후 cnt 더하기
=> 그냥 내가 처음 오해한 모양대로 인형 쌓고 그대로 하기?
"""

def make_board(raw_board):
    board = [[] for i in range(len(raw_board))]
    for j in range(len(raw_board)-1,-1,-1):
        raw = raw_board[j]
        for i in range(len(raw)):
            board[i].append(raw[i])
    return board

def solution(board, moves):
    board = make_board(board)
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

def 언제풀었는지모르겠는_예전풀이(board, moves):
    # 테스트케이스 1,2 런타임 에러남
    answer = 0
    stack = []
    top = 0

    for i in moves:  # len(moves)만큼 반복
        for j in range(0, len(board)):  # n x n의 n만큼 반복
            if(board[j][i-1] != 0):  # 검사하려는 열의(i) 맨 윗칸(n)부터 검사, 만약 비어있지 않다면
                if(top == board[j][i-1]):  # 만약 걸리는거랑 stack top에 있는 애가 같으면
                    stack.pop()  # pop하고
                    if not stack:
                        top = 0
                    else:
                        top = stack[-1]  # top바뀜
                    answer += 2  # pop한 인형 개수 추가됨
                    board[j][i-1] = 0  # 인형뽑기 인형 뽑힘
                    break
                else:  # 비어있지 않은데 stack top이랑 다르면
                    stack.append(board[j][i-1])  # stack에 넣어줌
                    top = stack[-1]
                    board[j][i-1] = 0
                    break
        # print(board)
        # print(stack)
    return answer
