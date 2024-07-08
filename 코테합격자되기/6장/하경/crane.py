def solution(board, moves):
    stack = [[] for _ in range(len(board))]
    basket = []
    count = 0

    for i in range(len(board) - 1, -1, -1): # 각 컬럼마다 스택 생성
        for j in range(len(board)):
            if board[i][j]:
                stack[j].append(board[i][j])

    for i in moves:
        if not stack[i - 1]:  # 스택이 비었을 경우
            pass
        elif not basket or stack[i-1][-1] != basket[-1] and basket: # 바구니가 비었거나 맨 위 인형과 다른 경우
            basket.append(stack[i-1].pop())
        elif basket and stack[i-1][-1] == basket[-1] and basket: # 바구니가 차있고 기존 맨 위 인형과 동일한 경우
            stack[i-1].pop()
            basket.pop()
            count += 2

    return count

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))