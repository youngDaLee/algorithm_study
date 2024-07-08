from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while(goal): # goal 요소의 개수만큼 반복
        word = goal.popleft()
        if cards1 and cards1[0] == word:
            cards1.popleft()
        if cards2 and cards2[0] == word:
            cards2.popleft()
        print((cards1, cards2))

    if len(cards1) == 0 and len(cards2) == 0:
        return True
    else:
        return False


cards1 = list(input().split())
cards2 = list(input().split())
goal = list(input().split())

print(solution(cards1, cards2, goal))