"""
문제
* 정수 배열 numbers에서 서로 다른 인덱스 2개 수를 뽑아 더해 만들 수 있는 모든 수

권장 시간복잡도
* O(N^2log(N^2))

내 풀이
* 모든 경우의 수를 순회하여 더한 데이터를 set에 저장
    * O(N^2)
* set의 데이터를 정렬
    * O(NlogN)
* 총 시간복잡도 O(N^2 + NlogN) = O(N^2)
"""

def solution(number):
    s = set()
    for i in range(len(number)):
        for j in range(i, len(number)):
            s.add(number[i] + number[j])

    li = sorted(list(s))
    return li
