"""
문제
* 카드 단어를 이용해 배열 만들 수 있는지 알고싶음
* 조건
    * 카드 뭉치에서 카드를 순서대로 한장씩 사용
    * 한 번 사용한 카드는 다시 사용할 수 없음
    * 카드를 사용하지 않고 다음 카드로 넘길 수 없음
    * 기존 카드 뭉치 단어 순서 바꿀 수 없음

권장 시간복잡도
* O(N+M)

내 풀이
* 카드를 popleft, append하면서 돌아확인 -> 어차피 카드 뭉치 두개로 정해져 있으니까 그냥 굳이 데큐 만들지 않기
* 해당 리스트 top의 값이 원하는 값이면 pop, 아니면 다음 카드 뭉치 확인
* 큐보다는 스택같은데?
    * 다만... reverse는 O(n), pop(0) 도 O(n) 이니까 그냥 deque 쓰는게 효율적
"""
from collections import deque


def solution(cards1, cards2, goals):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goals = deque(goals)

    while goals:
        word = goals.popleft()
        if cards1 and cards1[0] == word:
            cards1.popleft()
            continue
        elif cards2 and cards2[0] == word:
            cards2.popleft()
            continue
        else:
            return False
    return True


print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))