"""
문제
* 배열 중복값 제거하고 배열 데이터 내림차순 정렬

권장 시간복잡도
* O(NlogN)

내 풀이
* set으로 중복값 제거하고 .sort() 내장함수로 정렬
    * set은 O(N)
    * .sort는 O(NlogN)으로
    * 총 시간 복잡도는 O(N + NlogN) = O(NlogN)
"""

def solution(li):
    li = list(set(li))
    li.sort(reverse=True)
    return li
