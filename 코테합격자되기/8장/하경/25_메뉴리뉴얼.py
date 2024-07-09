'''
N개 선택된 메뉴들 중에 가장 빈도가 많은 조합을 찾아내는 문제
-> itertools 라이브러리의 combinations 함수
찾아낸 조합들의 빈도수(등장 개수)를 카운트 해야 함.
-> collections 모듈의 Counter 클래스
Counter 클래스는 각 요소들(key)의 개수(value)를 딕셔너리 자료형으로 저장하여 반환함.
==============
key | val
--------------
('A', 'B')  |  2
('B', 'C')  |  3
('A', 'B', 'D')   |  4
('A', 'B', 'C', 'D'))  |  1
==============
Counter 클래스가 딕셔너리 자료형이므로 해시구조가 맞지만, 이 문제를 보고
'이건 해시다!'라고 생각하기보다는 '조합'과 '개수 효율적으로 세기'를 빠르게 떠올리는 것이 더 나을 것 같음.
*다만 combinations 함수는 순서를 고려하므로 대상 리스트를 항상 sort하여 통일성 보장할 것!
'''
from itertools import combinations # 조합
from collections import Counter # 개수 세기

def solution(orders, course):
    res = []

    for c in course:
        menu = []
        for order in orders:
            comb = combinations(sorted(order), c)
            menu += comb

        counter = Counter(menu) # 자료 안에 각 요소들이 몇 개가 있는지를 딕셔너리로 저장해줌
        if (max(counter.values()) != 1): # 2번 이상 주문되어야 함
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    res.append("".join(m))

    return sorted(res)


orders = eval(input())
course = eval(input())
print(solution(orders, course))